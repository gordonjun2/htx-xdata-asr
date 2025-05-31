import requests
import pandas as pd
from utils import logger, list_files_in_directory

skipped_files = []


def get_transcription_from_asr_api(file_path,
                                   api_url='http://localhost:8001/asr'):

    with open(file_path, 'rb') as f:
        file = {'file': (file_path, f, 'audio/mpeg')}
        response = requests.post(api_url, files=file)

    if response.status_code == 200:
        response_data = response.json()
        data = response_data.get('data', {})
        transcription = data.get('transcription', '')
        duration = data.get('duration', 0)
        logger.info(
            f"\nProcessed audio file: {file_path.split('/')[-1]}\nTranscription: {transcription}\nDuration: {duration}s\n"
        )
    else:
        logger.error(
            f"\nCode: {response.status_code}\nMessage: {response.text}\n")
        skipped_files.append(file_path)
        transcription = ''

    return transcription


if __name__ == "__main__":
    dataset_split = 'cv-valid-dev'
    files_directory = f'../datasets/common_voice/{dataset_split}/{dataset_split}'
    files = list_files_in_directory(files_directory)
    api_url = 'http://localhost:8001/asr'

    cv_csv_file = f'../datasets/common_voice/{dataset_split}.csv'
    df = pd.read_csv(cv_csv_file)
    df['exact_filename'] = df['filename'].str.split('/').str[-1]
    df['generated_text'] = ''

    for file_path in files:
        transcription = get_transcription_from_asr_api(file_path, api_url)
        current_exact_filename = file_path.split('/')[-1]
        df.loc[df['exact_filename'] == current_exact_filename,
               'generated_text'] = transcription

    df = df.drop('exact_filename', axis=1)

    output_csv = f'./{dataset_split}-with-generated-text.csv'
    df.to_csv(output_csv, index=False)

    logger.info(f"Transcriptions saved to {output_csv}")

    if skipped_files:
        skipped_files_output_txt = 'cv-decode_skipped_files.txt'
        with open(skipped_files_output_txt, 'w') as f:
            for file_path in skipped_files:
                f.write(f"{file_path}\n")

        logger.warning(
            f"Some files were skipped due to errors. Check '{skipped_files_output_txt}' for the files."
        )

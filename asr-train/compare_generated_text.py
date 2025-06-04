import pandas as pd
from jiwer import wer, cer


def compute_scores(row):
    label = row['text']
    pred = row['generated_text']
    finetuned_pred = row['finetuned_generated_text']

    return pd.Series({
        'wer_score': wer(label, pred),
        'cer_score': cer(label, pred),
        'finetuned_wer_score': wer(label, finetuned_pred),
        'finetuned_cer_score': cer(label, finetuned_pred),
    })


cv_csv_file = './cv-valid-dev-with-finetuned-generated-text.csv'
df = pd.read_csv(cv_csv_file)
df['text'] = df['text'].str.upper()
df[['generated_text', 'finetuned_generated_text'
    ]] = df[['generated_text', 'finetuned_generated_text']].fillna('')

df[['wer_score', 'cer_score', 'finetuned_wer_score',
    'finetuned_cer_score']] = df.apply(compute_scores, axis=1)

overall_wer = df['wer_score'].mean()
overall_cer = df['cer_score'].mean()
overall_finetuned_wer = df['finetuned_wer_score'].mean()
overall_finetuned_cer = df['finetuned_cer_score'].mean()

print(f"Overall WER: {overall_wer:.4f}")
print(f"Overall CER: {overall_cer:.4f}")
print(f"Overall Finetuned WER: {overall_finetuned_wer:.4f}")
print(f"Overall Finetuned CER: {overall_finetuned_cer:.4f}")

output_csv = f'./cv-valid-dev-with-finetuned-generated-text.csv'
df.to_csv(output_csv, index=False)

print(f"Results saved to {output_csv}")

# Terminal Output:
"""
Overall WER: 0.1176
Overall CER: 0.0492
Overall Finetuned WER: 0.0426
Overall Finetuned CER: 0.0182
Results saved to ./cv-valid-dev-with-finetuned-generated-text.csv
"""

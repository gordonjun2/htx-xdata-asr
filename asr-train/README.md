# htx-xdata-asr

## Task 3a Usage Instruction

- Run the Jupyter Notebook below:
  ```
  jupyter notebook cv-train-2a.ipynb
  ```
- Go through the notebook and execute all the cells inside.

## Task 3b Usage Instruction

- Copy the finetuned model from Task 3a (inside _./checkpoints_) to a new folder called _./saved_models_.
- Rename the finetuned model to _wav2vec2-large-960h-cv_.

## Task 3c Usage Instruction

- The codes to complete this task is also in _cv-train-2a.ipynb_.
- Run the Jupyter Notebook below:
  ```
  jupyter notebook cv-train-2a.ipynb
  ```
- Go through the notebook and execute all the cells inside.
- The file _cv-valid-test-with-generated-text.csv_ will be generated, with all the transcription copied to the new column _generated_text_.

## Task 4 Usage Instruction

- Copy the _cv-valid-dev-with-generated-text.csv_ from Task 2d in _./asr_ folder to this directory.
- Run the code below:
  ```
  python cv-decode.py
  ```
- The file _cv-valid-dev-with-finetuned-generated-text.csv_ will be generated, with all the transcription from the finetuned model copied to the new column _finetuned_generated_text_.
- Run the code below:
  ```
  compare_generated_text.py
  ```
- The file _cv-valid-dev-with-finetuned-generated-text.csv_ will be updated with the evaluation scores.
- The _training-report.pdf_ is created and saved in the main directory of this repository.

## Deliverables in this Directory

- _cv-train-2a.ipynb_ for Task 3a and 3c
- _./saved_models/wav2vec2-large-960h-cv_ for Task 3b
- _cv-valid-test-with-generated-text.csv_ for Task 3c
- _cv-valid-dev-with-finetuned-generated-text.csv_ for Task 4

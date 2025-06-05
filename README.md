# htx-xdata-asr

## Repository Structure

- _./asr_ contains:
  - Task 2
- _./asr-train_ contains:
  - Task 3
  - Task 4
- _./hotword-detection_ contains:
  - Task 5
- _datasets_ should contain:
  - _common_voice_ dataset directory downloaded from [this link](https://www.dropbox.com/scl/fi/i9yvfqpf7p8uye5o8k1sj/common_voice.zip?rlkey=lz3dtjuhekc3xw4jnoeoqy5yu&dl=0)
- _training-report.pdf_ is for Task 4 as well
- _essay-ssl.pdf_ is for Task 6

## Deliverables in this Directory

- _training-report.pdf_ for Task 4
- _essay-ssl.pdf_ for Task 6

## Usage Instruction

- Create a Python virtual environment for this project.
  ```
  python3 -m venv venv
  ```
- Activate the Python virtual environment.
  ```
  source venv/bin/activate
  ```
- Install required packages.
  ```
  pip install -r requirements.txt
  ```
- Install a Python kernel for Jupyter Notebooks.
  ```
  python -m ipykernel install --user
  ```
- Please `cd` into the respective folders to see their _README.md_.

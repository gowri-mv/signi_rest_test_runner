# signi_rest_test_runner

This project is a solution to the Signi5sys Internship Coding Challenge (August 2025).

It includes:
- A sample Flask API (`sample_api/app.py`)
- A YAML-driven REST API test runner (`src/signi_rest_test_runner/`)
- A working test scenario (`test_config.yaml`)
- AI usage declaration (`ai_usage.md`)
- Findings and debugging summary (`findings.md`)



## How to Run the Project

### 1. Install dependencies

```bash
pip install -r requirements.txt
(or manually install)
pip install flask httpx jinja2 jsonpath-ng pyyaml  


### 2. Run the Sample API
In a separate terminal:

bash
cd sample_api
python app.py
API runs at: http://127.0.0.1:5000

### 3. Run the Test Runner
bash
cd src/signi_rest_test_runner
python runner.py ../../test_config.yaml


### Expected Output
The test runner should:
-Send a GET request to /status
-Validate the HTTP status and response JSON

Results are saved in:
test_results/output.txt

### Directory Overview
├── sample_api/              # Simple Flask API
├── src/signi_rest_test_runner/   # Test runner code
├── test_config.yaml         # Scenario definition
├── test_results/output.txt  # Test output
├── ai_usage.md              # AI usage declaration
├── findings.md              # Debugging notes
└── README.md                # This file

### Author
Gowri M V
Submission for Signi5sys Internship Coding Challenge – August 2025

##  Final Checklist Before Submission

- [x] `test_config.yaml`
- [x] `test_results/output.txt`
- [x] `findings.md`
- [x] `README.md`
- [x] `ai_usage.md`
- [x] Code pushed to GitHub
- [x] Repo made public or shared with `signi5code`
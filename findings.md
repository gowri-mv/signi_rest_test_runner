# Findings & Debug Notes

## 1. Import Path Errors
The test runner used absolute imports like `from src...`, which failed when running the file directly. I resolved this by switching to relative imports (`from executor import ...`) and running the script directly from the `src/signi_rest_test_runner` folder.

## 2. test_config.yaml Format
Initially, I used a test structure with a `tests:` key. However, the runner expected a top-level `steps:` key. I corrected the YAML structure to:

```yaml
name: Check /status
steps:
  - name: GET /status
    request:
      method: GET
      url: http://127.0.0.1:5000/status
    assert:
      status_code: 200
      body:
        message: "API is working"

## 3. Connection Refused Error
I faced a [WinError 10061] because the Flask API wasn't running when I ran the tests. I fixed this by starting the API in a separate terminal with:
python app.py
 
 4. Output Verification
After correcting the YAML and running the API, the runner successfully made a request and validated the response.

# Directory Structure:
# rest_api_test_runner/
# ├── runner.py
# ├── scenario_loader.py
# ├── executor.py
# ├── validator.py
# ├── utils.py
# └── scenarios/example.yaml

# ---- runner.py ----
import sys
from scenario_loader import load_scenario
from executor import execute_scenario
from validator import validate_scenario

if __name__ == '__main__':
    scenario_path = (
        sys.argv[1] if len(sys.argv) > 1 else "scenarios/example.yaml"
    )

    with open(scenario_path, 'r') as f:
        raw_yaml = f.read()
        print("📄 RAW YAML:\n", raw_yaml)

    scenario = load_scenario(scenario_path)
    print("✅ Scenario Loaded:", scenario)

    results = execute_scenario(scenario)
    validate_scenario(results)

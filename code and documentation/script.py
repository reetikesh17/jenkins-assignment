import os

print("--------------------------------------------------")
print("Hello! This is the Python script running in Jenkins.")
print("--------------------------------------------------")

# 1. Create a folder for test reports if it doesn't exist
output_dir = "test-reports"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 2. Create a dummy JUnit XML file
# This is required for the "Publish JUnit test result report" step to work.
xml_content = """<?xml version="1.0" encoding="UTF-8"?>
<testsuite name="Jenkins_PartC_Task4" tests="1" failures="0" errors="0" skipped="0" time="0.1">
    <testcase classname="ScriptTest" name="test_execution" time="0.1"/>
</testsuite>
"""

file_path = os.path.join(output_dir, "results.xml")
with open(file_path, "w") as f:
    f.write(xml_content)

print(f"SUCCESS: Generated test report at {file_path}")

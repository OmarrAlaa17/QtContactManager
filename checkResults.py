import re
import sys

with open('results.xml', 'r') as f:
    f.readline()
    summary = f.readline()
    # Extract values for tests and passes using regex
    match = re.search(r'tests="(\d+)"', summary)
    tests = int(match.group(1)) if match else None

    match = re.search(r' passes="(\d+)"', summary)
    passes = int(match.group(1)) if match else None

    # Check if tests equals passes
    if tests is not None and passes is not None:
        if tests == passes:
            print("The number of tests is equal to the number of passes.")
        else:
            sys.exit(1)
            print(f"The number of tests ({tests}) is not equal to the number of passes ({passes}).")
    else:
        print("Could not find the required attributes in the string.")
import os

# Change this to any folder you want
path = r"e:\PYTHON-PRACTICE"

# List all entries in the directory
entries = os.listdir(path)

print(f"Contents of '{path}':")
for name in entries:
    print(name)
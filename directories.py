from pathlib import Path

path = Path("modules")
path_fake = Path("fake_path")

print(path.exists())  # True
print(path_fake.exists())  # False

# Create a Path and then delete it

path = Path("email")
path.mkdir()  # You can't create the same path twice
path.rmdir()

# Loop over all folders and find .py files
path_assignments = Path("assignments")
for file in path_assignments.glob('*.py'):
    print(file)

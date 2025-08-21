import os

# Create a directory (will not error if it already exists)
directory_name = "my_new_directory"
os.makedirs(directory_name, exist_ok=True)
print(f"Directory '{directory_name}' created successfully.")

# List files and directories in the current directory
current_directory_contents = os.listdir(".")
print("Contents of current directory:", current_directory_contents)

# Create a directory with a full path
parent_directory = r"C:\Users\Sonu Kumar\OneDrive\Documents\GitHub\Kg\Kg"
full_directory_path = os.path.join(parent_directory, "another_directory")
os.makedirs(full_directory_path, exist_ok=True)

# List contents of a specific directory
target_directory = parent_directory  # Fixed: use a valid existing directory
if os.path.isdir(target_directory):
    target_directory_contents = os.listdir(target_directory)
    print(f"Contents of '{target_directory}':", target_directory_contents)
else:
    print(f"Directory '{target_directory}' does not exist.")

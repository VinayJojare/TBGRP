import os

directory = r"G:\Internships\TrustingBrains\cat vs dog\dataset\dogs"
prefix = "dog"  # You can customize the prefix if needed

# Iterate over files in the directory
for count, filename in enumerate(os.listdir(directory), start=1):
    # Create a new filename with the desired prefix and numeric count
    new_filename = f"{prefix}{count}.jpg"  # Change the extension if needed
    old_path = os.path.join(directory, filename)
    new_path = os.path.join(directory, new_filename)

    # Rename the file
    os.rename(old_path, new_path)

print("Bulk renaming completed.")

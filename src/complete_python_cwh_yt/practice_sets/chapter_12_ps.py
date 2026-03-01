# ----------------------------------------------------------------------------------------------------------------------------------------------

# 1. Write a Python program to open 3 different files using a context manager and if any of these files is not found then stop the program gracefully an print a message to the user.

try:
    with open("file1.txt", "r") as file1, open("file2.txt", "r") as file2, open(
        "file3.txt", "r"
    ) as file3:
        print("All files opened successfully.")
except FileNotFoundError as e:
    print(f"File not found: {e.filename}. Please check the file name and try again.")
    print(f"Error details: {e}")

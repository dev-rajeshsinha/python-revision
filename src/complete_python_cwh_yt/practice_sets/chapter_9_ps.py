# -------------------------------------------------------------------------------------------------------------------------------------------

# 1. Write a Python program to write 5 lines to a file and then read the file and print its contents. Also, update the file by adding 2 more lines to it and print the updated contents. Then update the second and fourth lines of the file and print the updated contents. Lastly, delete the file.

with open("../resources/file.txt", "w") as f:
    f.write("Line 1\n")
    f.write("Line 2\n")
    f.write("Line 3\n")
    f.write("Line 4\n")
    f.write("Line 5\n")

with open("../resources/file.txt", "r") as f:
    contents = f.read()
    print("Contents of the file:")
    print(contents)

with open("../resources/file.txt", "a") as f:
    f.write("Line 6\n")
    f.write("Line 7\n")

with open("../resources/file.txt", "r") as f:
    lines = f.readlines()
    print("Updated contents of the file:")
    for line in lines:
        print(line, end="")
    lines[1] = "Updated Line 2\n"
    lines[3] = "Updated Line 4\n"
    print()

with open("../resources/file.txt", "w") as f:
    f.writelines(lines)

with open("../resources/file.txt", "r") as f:
    contents = f.read()
    print("Updated contents of the file after modifying specific lines:")
    print(contents)

import os

os.remove("../resources/file.txt")

# -------------------------------------------------------------------------------------------------------------------------------------------

# 2. There is a file named "logs.txt" that contains users data logs. Read the file and wherever you find any email or password, replace it with "REDACTED". The emails will be preceded by the word "Email:" and the passwords will be preceded by the word "Password:". Once the update is done, save the updated contents of the logs in a new log file.

import re

with open("../resources/logs.txt", "r") as f:
    contents = f.read()

updated_contents = re.sub(r"(Email:\s*\S+)", "Email: REDACTED", contents)
updated_contents = re.sub(r"(Password:\s*\S+)", "Password: REDACTED", updated_contents)
print("Updated contents of the log file, with sensitive information redacted.")

with open("../resources/updated_logs.txt", "w") as f:
    f.write(updated_contents)

print()

# -------------------------------------------------------------------------------------------------------------------------------------------

# 3. Write a Python program to compare the file "main.txt" with "version_1.txt" and "version_2.txt". Compare the contents of the files and print the result as follows in a file named "differences.txt":
# - If "version_1.txt" is the same as "main.txt", print "Version 1 is the same as main"
# - If "version_2.txt" is the same as "main.txt", print "Version 2 is the same as main"
# - If any of the versions is different from "main.txt", print the line number and the difference in the format "Line X: main.txt vs version_Y.txt" for each line that is different.


def read_file(file_path):
    with open(file_path, "r") as f:
        return f.readlines()


main_lines = read_file("../resources/main.txt")
version_1_lines = read_file("../resources/version_1.txt")
version_2_lines = read_file("../resources/version_2.txt")

differences = []

if main_lines == version_1_lines:
    differences.append("Version 1 is the same as main")
else:
    for i in range(min(len(main_lines), len(version_1_lines))):
        if main_lines[i] != version_1_lines[i]:
            differences.append(f"Line {i + 1}: main.txt vs version_1.txt")

if main_lines == version_2_lines:
    differences.append("Version 2 is the same as main")
else:
    for i in range(min(len(main_lines), len(version_2_lines))):
        if main_lines[i] != version_2_lines[i]:
            differences.append(f"Line {i + 1}: main.txt vs version_2.txt")

with open("../resources/differences.txt", "w") as f:
    for difference in differences:
        f.write(difference + "\n")

print()

# -------------------------------------------------------------------------------------------------------------------------------------------

# 4. Write a Python program to make a copy of a file named "main.txt" and name the copy "destination.txt". Then, read the contents of both files and verify that the copy was successful. Lastly, delete the copied file "destination.txt".

import shutil

shutil.copy("../resources/main.txt", "../resources/destination.txt")

with open("../resources/main.txt", "r") as f:
    main_contents = f.read()

with open("../resources/destination.txt", "r") as f:
    destination_contents = f.read()

if main_contents == destination_contents:
    print("The copy was successful. Both files have the same contents.")
else:
    print("The copy was not successful. The contents of the files are different.")

import os

os.remove("../resources/destination.txt")

print()

# Notes: The shutil module provides a higher-level interface for file operations, including copying files. The shutil.copy() function is used to copy the contents of "main.txt" to "destination.txt". Other useful functions in the shutil module include shutil.copy2() for copying files along with their metadata, shutil.move() for moving files, and shutil.rmtree() for deleting directories and their contents.

# -------------------------------------------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------------------------------------

# File I/O in Python is a powerful feature that allows us to read from and write to files on our computer or to any remote server. This is essential for tasks such as data storage, configuration management, and more. The reason we need to learn file I/O is that it enables us to persist data beyond the runtime of our program, making it possible to save user input, log information, and work with large datasets. Usually, when we deal with data in our programs, it gets stored in memory, which is temporary. If we want to keep that data for future use, we need to write it to a file. Similarly, if we want to use data that was previously saved, we need to read it from a file. This is where file I/O comes into play. There are also a variety of file formats (like text files, CSV files, JSON files, etc.) that we can work with, and Python provides built-in support for handling these formats efficiently.

# -------------------------------------------------------------------------------------------------------------------------------------------

# In Python, we can perform file I/O operations using the built-in `open()` function. This function allows us to open a file in various modes (like write, read, append, etc.) and returns a file object that we can use to interact with the file. We use the open function along with the `with` statement to ensure that the file is properly closed after we're done with it, even if an error occurs. This is a best practice in Python for handling files.

# Opening a file in write mode ("w") will create the file if it doesn't exist or overwrite it if it does.

with open("../resources/example.txt", "w") as file:
    print("File opened successfully in write mode.")
    file.write("Hello, this is a line of text.\n")
    file.write("This is another line of text.\n")
    print(
        "Data has been written to the file and the file has been closed automatically."
    )
    print()  # Just to add a newline for better readability in the output.

# Opening a file in read mode ("r") allows us to read the contents of the file.

with open("../resources/example.txt", "r") as file:
    print("File opened successfully in read mode.")
    content = file.read()
    print(content)
    print("File has been read successfully and closed automatically.")
    print()  # Just to add a newline for better readability in the output.

# Opening a file in append mode ("a") allows us to add new content to the end of the file without overwriting the existing content.

with open("../resources/example.txt", "a") as file:
    print("File opened successfully in append mode.")
    file.write("This line is appended to the file.\n")
    print(
        "New data has been appended to the file and the file has been closed automatically."
    )
    print()  # Just to add a newline for better readability in the output.

# We can also read the file again to see the updated content.

with open("../resources/example.txt", "r") as file:
    print("File opened successfully in read mode to check appended content.")
    content = file.read()
    print(content)
    print("File has been read successfully and closed automatically.")
    print()  # Just to add a newline for better readability in the output.

# We can also update the content of a file by opening it in read and write mode ("r+"). This allows us to read the existing content and then write new content to the file without overwriting it completely.

with open("../resources/example.txt", "r+") as file:
    print("File opened successfully in read and write mode.")
    content = file.read()
    print("Current content of the file:")
    print(content)
    file.seek(0)  # Move the cursor to the beginning of the file
    file.write("This line replaces the first line of the file.\n")
    print(
        "The first line of the file has been updated and the file has been closed automatically."
    )
    print()  # Just to add a newline for better readability in the output.

# -------------------------------------------------------------------------------------------------------------------------------------------

# When we use the `read()` method on a file object, it reads the entire content of the file as a single string and returns the whole content at once. This can be useful for small files, but it may not be efficient for larger files as it can consume a lot of memory. In case of larger files, it is often better to read the file line by line using a loop or to read a specific number of characters at a time. For that purpose, we can use the `readline()` method to read one line at a time or the `readlines()` method to read all lines into a list. This way, we can process the file content more efficiently without loading the entire file into memory at once.

# Reading a file line by line using readline(), which works as an iterator and returns one line at a time until the end of the file is reached.

with open("../resources/example.txt", "r") as file:
    print("Reading the file line by line using readline():")
    line = file.readline()
    while line:
        print(line, end="")  # end="" to avoid adding extra newlines
        line = file.readline()
    print("\nFile has been read successfully and closed automatically.")
    print()  # Just to add a newline for better readability in the output.

# Reading all lines into a list using readlines(), which returns a list of lines from the file.

with open("../resources/example.txt", "r") as file:
    print("Reading all lines into a list using readlines():")
    lines = file.readlines()
    for line in lines:
        print(line, end="")  # end="" to avoid adding extra newlines
    print("\nFile has been read successfully and closed automatically.")
    print()  # Just to add a newline for better readability in the output.

# -------------------------------------------------------------------------------------------------------------------------------------------

# We can also work with files in binary mode by using "rb" for reading and "wb" for writing. This is particularly useful when dealing with non-text files such as images, audio files, or any other type of binary data. When we open a file in binary mode, the data is read or written as bytes rather than strings. This allows us to handle the raw data directly without any encoding or decoding issues that can arise with text files.

# Reading a file in binary mode.

with open("../resources/sample_image.jpg", "rb") as file:
    print("Image file opened successfully in binary read mode.")
    binary_content = file.read()
    print(binary_content)
    print("Image file has been read successfully and closed automatically.")
    print()  # Just to add a newline for better readability in the output.


# Writing to a file in binary mode.

with open("../resources/new_image.jpg", "wb") as file:
    print("Image file opened successfully in binary write mode.")
    # Here we would write binary data to the file. For demonstration, we will just write the same content we read from the previous image.
    file.write(binary_content)
    print(
        "Binary data has been written to the new image file and the file has been closed automatically."
    )
    print()  # Just to add a newline for better readability in the output.

# Similar to reading from and writing to binary files, we can append to binary files using "ab" mode, which allows us to add new binary data to the end of an existing file without overwriting it.

with open("../resources/new_image.jpg", "ab") as file:
    print("Image file opened successfully in binary append mode.")
    # Here we would append binary data to the file. For demonstration, we will just write the same content again to show that it is being appended.
    file.write(binary_content)
    print(
        "Binary data has been appended to the new image file and the file has been closed automatically."
    )
    print()  # Just to add a newline for better readability in the output.

# -------------------------------------------------------------------------------------------------------------------------------------------

# In addition to the basic file I/O operations, Python provides several other useful functions and methods for working with files. For example, we can use the `os` module to perform various file-related operations such as checking if a file exists, getting the size of a file, or deleting a file. The `os.path` module provides functions for manipulating file paths, such as joining paths, splitting paths, and checking if a path is a file or a directory. These additional functionalities make it easier to manage files and directories in our Python programs.

import os

# Joining paths using os.path.join()
directory = "../resources"
filenames = ("example.txt", "new_image.jpg")
for filename in filenames:
    full_path = os.path.join(directory, filename)
    print(f"The full path to the file is: {full_path}")

    # Checking if a file exists using os.path.exists()
    if os.path.exists(full_path):
        print(f"The file '{full_path}' exists.")

        # Checking if a path is a file or a directory using os.path.isfile() and os.path.isdir()
        if os.path.isfile(full_path):
            print(f"The path '{full_path}' is a file.")
        elif os.path.isdir(full_path):
            print(f"The path '{full_path}' is a directory.")
        else:
            print(f"The path '{full_path}' is neither a file nor a directory.")

        # Getting the size of a file using os.path.getsize()
        file_size = os.path.getsize(full_path)
        print(f"The size of the file '{full_path}' is {file_size} bytes.")

        # Deleting a file using os.remove()
        os.remove(full_path)
        print(f"The file '{full_path}' has been deleted.")
    else:
        print(f"The file '{full_path}' does not exist.")
    print()  # Just to add a newline for better readability in the output.

# -------------------------------------------------------------------------------------------------------------------------------------------

# We can also work with csv files using the built-in `csv` module in Python. This module provides functionality to read from and write to CSV files, which are commonly used for storing tabular data. The `csv` module allows us to easily handle CSV files by providing functions to read and write data in a structured way, making it easier to work with data in a tabular format.

import csv

# Writing to a CSV file using csv.writer()

with open("../resources/example.csv", "w", newline="") as file:
    print("CSV file opened successfully in write mode.")
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Alice", 30, "New York"])
    writer.writerow(["Bob", 25, "Los Angeles"])
    print(
        "Data has been written to the CSV file and the file has been closed automatically."
    )
    print()  # Just to add a newline for better readability in the output.

# Reading from a CSV file using csv.reader()

with open("../resources/example.csv", "r") as file:
    print("CSV file opened successfully in read mode.")
    reader = csv.reader(file)
    for row in reader:
        print(row)
    print("CSV file has been read successfully and closed automatically.")
    print()  # Just to add a newline for better readability in the output.

# We can also use csv.DictWriter() and csv.DictReader() to work with CSV files using dictionaries, which can be more convenient when dealing with data that has headers.

with open("../resources/example.csv", "w", newline="") as file:
    print("CSV file opened successfully in write mode using DictWriter.")
    fieldnames = ["Name", "Age", "City"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"Name": "Alice", "Age": 30, "City": "New York"})
    writer.writerow({"Name": "Bob", "Age": 25, "City": "Los Angeles"})
    print(
        "Data has been written to the CSV file using DictWriter and the file has been closed automatically."
    )
    print()  # Just to add a newline for better readability in the output.

with open("../resources/example.csv", "r") as file:
    print("CSV file opened successfully in read mode using DictReader.")
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
    print(
        "CSV file has been read successfully using DictReader and closed automatically."
    )
    print()  # Just to add a newline for better readability in the output.

# -------------------------------------------------------------------------------------------------------------------------------------------

# We can also work with JSON files using the built-in `json` module in Python. This module provides functionality to read from and write to JSON files, which are commonly used for storing structured data in a human-readable format. The `json` module allows us to easily handle JSON files by providing functions to serialize and deserialize data, making it easier to work with data in a structured format.

import json

# Writing to a JSON file using json.dump()

with open("../resources/example.json", "w") as file:
    print("JSON file opened successfully in write mode.")
    data = {
        "name": "Alice",
        "age": 30,
        "city": "New York",
        "hobbies": ["reading", "traveling", "cooking"],
    }
    json.dump(data, file, indent=4)
    print(
        "Data has been written to the JSON file and the file has been closed automatically."
    )
    print()  # Just to add a newline for better readability in the output.

# Reading from a JSON file using json.load()

with open("../resources/example.json", "r") as file:
    print("JSON file opened successfully in read mode.")
    data = json.load(file)
    print(data)
    print("JSON file has been read successfully and closed automatically.")
    print()  # Just to add a newline for better readability in the output.

# We can also use json.dumps() and json.loads() to work with JSON data as strings, which can be useful when we want to handle JSON data without writing it to a file.

data = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "traveling", "cooking"],
}

# Serializing data to a JSON string using json.dumps()

json_string = json.dumps(data, indent=4)
print("Data has been serialized to a JSON string:")
print(json_string)
print()  # Just to add a newline for better readability in the output.

# Deserializing data from a JSON string using json.loads()

deserialized_data = json.loads(json_string)
print("Data has been deserialized from the JSON string:")
print(deserialized_data)
print()  # Just to add a newline for better readability in the output.

# -------------------------------------------------------------------------------------------------------------------------------------------

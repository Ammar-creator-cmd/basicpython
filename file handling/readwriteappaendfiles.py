def write(textfile, text):
    try:
        with open(textfile, "w") as file:
            file.write(text)
        print(f"Text written to {textfile} successfully.")
    except Exception as e:
        print(f"An error occurred while writing to {textfile}: {e}")

"""write("test.txt", "This is a test file.")"""

def read(textfile):
    try:
        with open(textfile, "r") as file:
            content = file.read()
        print(f"Content of {textfile}:")
        print(content)
    except FileNotFoundError:
        print(f"The file {textfile} does not exist.")
    except Exception as e:
        print(f"An error occurred while reading {textfile}: {e}")

read("test.txt")

def append(textfile, text):
    try:
        with open(textfile, "a") as file:
            file.write(text)
        print(f"Text appended to {textfile} successfully.")
    except Exception as e:
        print(f"An error occurred while appending to {textfile}: {e}")
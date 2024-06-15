def write_to_file():
  """Creates a new text file and writes content to it."""
  try:
    with open("my_file.txt", "w") as file:
      file.write("Line 1: This is some text.\n")
      file.write("Line 2: Numbers can be written too: 42\n")
      file.write("Line 3: Mixing data types is possible.\n")
  except PermissionError:
    print("Error: Insufficient permissions to write to the file.")
  except Exception as e:
    print(f"An unexpected error occurred while writing: {e}")

def read_from_file():
  """Reads the contents of a text file and displays them."""
  try:
    with open("my_file.txt", "r") as file:
      contents = file.read()
      print(contents)
  except FileNotFoundError:
    print("Error: The file 'my_file.txt' does not exist.")
  except Exception as e:
    print(f"An unexpected error occurred while reading: {e}")

def append_to_file():
  """Opens a text file in append mode and writes additional content."""
  try:
    with open("my_file.txt", "a") as file:
      file.write("\nLine 4: Appending more text.\n")
      file.write("Line 5: Here's another line.\n")
      file.write("Line 6: This demonstrates appending functionality.\n")
  except PermissionError:
    print("Error: Insufficient permissions to write to the file.")
  except Exception as e:
    print(f"An unexpected error occurred while appending: {e}")

# Call the functions to perform file operations
write_to_file()
read_from_file()
append_to_file()
read_from_file()  # Read again to show appended content

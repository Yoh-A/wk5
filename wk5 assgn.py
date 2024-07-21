# File Creation
try:
    # Open 'my_file.txt' in write mode ('w')
    with open('my_file.txt', 'w') as file:
        # Write three lines of text
        file.write("This is line 1\n")
        file.write("12345\n")
        file.write("Another line here\n")
    print("File 'my_file.txt' created and initial content written.")

    # File Reading and Display
    print("\nReading 'my_file.txt':")
    with open('my_file.txt', 'r') as file:
        content = file.read()
        print(content)

    # File Appending
    print("\nAppending to 'my_file.txt':")
    with open('my_file.txt', 'a') as file:
        file.write("Appended line 1\n")
        file.write("67890\n")
        file.write("Final line appended\n")
    print("Appended additional content to 'my_file.txt'.")

except FileNotFoundError:
    print("Error: The file 'my_file.txt' was not found.")

except PermissionError:
    print("Error: Permission denied to open 'my_file.txt'.")

finally:
    print("\nExecution completed.")

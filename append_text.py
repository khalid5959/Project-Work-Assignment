# Create a file object in append mode
with open("myfile.txt", "a") as f:
    # Append text to the file
    f.write("This is new text. ")

# Display the text in the file
with open("myfile.txt", "r") as f:
    text = f.read()
    print(text)

with open("myfile.txt", "r") as fp:
    lines = len(fp.readlines())
    print(f"Total Number of lines: {lines}")

import sys

if __name__ == "__main__":
    str = ""
    for index, char in enumerate(sys.argv[1]):
        str += chr(ord(char) - index)
    print(str)
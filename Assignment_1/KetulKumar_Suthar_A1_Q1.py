# Write a module that prints “hello world!” when it is run as main module and prints “from library module” when is used as a library module

def main():
    """This function called from main module
    """
    print("hello world!!")


if __name__ == '__main__':
    main()
else:
    print("from library module")

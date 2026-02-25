from functions.get_file_content import get_file_content


def main():
    res = get_file_content("calculator", "lorem.txt")
    print("Result for current file:")
    print(res)
    print("")

    res = get_file_content("calculator", "main.py")
    print("Result for current file:")
    print(res)
    print("")

    res = get_file_content("calculator", "pkg/calculator.py")
    print("Result for current file:")
    print(res)
    print("")

    res = get_file_content("calculator", "/bin/cat")
    print("Result for current file:")
    print(res)
    print("")

    res = get_file_content("calculator", "pkg/does_not_exist.py")
    print("Result for current file:")
    print(res)
    print("")


main()

import sys


def main():
    print(
        "Use terminal to navigate through 'directory' and find the flag. Don't enter 'Flag: ', simply the content of the flag.")
    password_guess = ''
    while password_guess != ctf_password:
        password_guess = input("Enter the flag: ")

    print("Congrats! That's the correct flag!")


if __name__ == '__main__':
    input_file = sys.argv[1]
    with open(input_file) as file:
        ctf_password = file.read()
    main()

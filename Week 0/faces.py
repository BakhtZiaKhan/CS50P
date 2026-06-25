def main():
    str = input("Type your input ")

    str = convert(str)

    print(str)

def convert(str):

    str = str.replace(":)", "🙂")

    str = str.replace(":(", "🙁")

    return str

main()

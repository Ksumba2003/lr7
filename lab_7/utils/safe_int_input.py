def safe_int_input(prompt=""):
    number = None
    while not number:
        try:
            number = int(input(prompt))
        except ValueError:
            print("Введено не число")
    return number

import pyperclip

while True:

    number = input("Valor: ")

    if number == "0":
        break

    number = number.replace(",", ".")

    number_float = float(number)
    soma = number_float + (number_float * 0.0638)

    number_str = round(soma, 2)
    number_copy = (str(number_str)).replace(".", ",")

    pyperclip.copy(number_copy)
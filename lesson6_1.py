#Написать функцию перевода десятичного числа в двоичное и обратно, без использования функции int

def converter(number, to_binary=True):
    if to_binary:
        # Перевод из десятичного в двоичное
        binary_result = ""
        while number > 0:
            remainder = number % 2
            binary_result = str(remainder) + binary_result
            number = number // 2
        return binary_result if binary_result != "" else "0"
    else:
        # Перевод из двоичного в десятичное
        binary_str = str(number)
        decimal_result = 0
        for i in range(len(binary_str)):
            if binary_str[i] == '1':
                decimal_result += 2**(len(binary_str) - i - 1)
        return decimal_result

decimal_number = 23
binary_representation = converter(decimal_number)
print(f"{decimal_number} в двоичной системе: {binary_representation}")

binary_number = "1011"
decimal_representation = converter(binary_number, to_binary=False)
print(f"{binary_number} в десятичной системе: {decimal_representation}")

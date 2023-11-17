#Написать функцию перевода десятичного числа в двоичное и обратно, без использования функции int

# def is_number(a):
#     a = 45
#     n = ""
#     s = ""
#     while a > 0:
#         n = str(a % 2) + n
#         a //= 2
#     return n
#
# print(is_number(a=45))
# def convert_to(number, base, upper=False):
#     digits = '0123456789abcdefghijklmnopqrstuvwxyz'
#     if base > len(digits):
#         return None
#     result = ''
#     while number > 0:
#         result = digits[number % base] + result
#         number //= base
#     return result.upper() if upper else result
#
# print(convert_to(100))
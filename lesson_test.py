input_filename = 'text.txt'
with open(input_filename, 'r', encoding='utf-8') as file:
    lines = file.readlines()

output_filename = 'результат.txt'
with open(output_filename, 'w', encoding='utf-8') as output_file:
    for i, line in enumerate(lines, 1):
        line = line.rstrip('\n')
        letter_count = sum(c.isalpha() for c in line)
        output_file.write(f"{i} строка - {letter_count} букв\n")

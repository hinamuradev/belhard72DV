def read_csv(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    headers = lines[0].strip().split(',')
    data = []
    for line in lines[1:]:
        values = line.strip().split(',')
        row_dict = dict(zip(headers, values))
        data.append(row_dict)

    return data
# Пример
csv_file_path = 'file.csv'
result = read_csv(csv_file_path)

for row in result:
    print(row)
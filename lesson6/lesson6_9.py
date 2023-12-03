# Дан словарь словарей, ключ внешнего словаря - id пользователя, значение -
# словарь с данными о пользователе (имя, фамилия, телефон, почта), вывести
# имена тех, у кого не указана почта (нет ключа email или значение этого ключа -пустая строка)
def find_users_without_email(user_data):
    users_email = []

    for user_id, user_info in user_data.items():
        if 'email' not in user_info or user_info['email'] == '':
            users_email.append(user_info.get('имя', 'Неизвестно'))

    return users_email

users_data = {
    1: {'имя': 'Иван', 'фамилия': 'Иванов', 'телефон': '123-456-789', 'email': 'ivan@example.com'},
    2: {'имя': 'Петр', 'фамилия': 'Петров', 'телефон': '987-654-321'},
    3: {'имя': 'Мария', 'фамилия': 'Сидорова', 'телефон': '555-123-456', 'email': 'maria@example.com'},
    4: {'имя': 'Анна', 'фамилия': 'Кузнецова', 'телефон': '777-888-999', 'email': ''}
}

users_emails = find_users_without_email(users_data)
print("Пользователи без указанной почты:")
for user_name in users_emails:
    print(user_name)

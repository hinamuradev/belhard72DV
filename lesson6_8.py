# Дан словарь, ключ - Название страны, значение - список городов, на вход
# поступает город, необходимо сказать из какой он страны
def find_country_by_city(city, countries_data):
    for country, cities in countries_data.items():
        if city in cities:
            return country
    return "Город не найден"

# Пример использования:
countries_and_cities = {
    "Россия": ["Москва", "Санкт-Петербург", "Новосибирск"],
    "США": ["Нью-Йорк", "Лос-Анджелес", "Чикаго"],
    "Франция": ["Париж", "Марсель", "Лион"],
    "Италия": ["Рим", "Милан", "Неаполь"]
}

city_to_find = "Милан"
found_country = find_country_by_city(city_to_find, countries_and_cities)

if found_country != "Город не найден":
    print(f"Город {city_to_find} находится в стране {found_country}.")
else:
    print(f"Город {city_to_find} не найден в списке стран.")
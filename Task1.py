# Напишите программу, удаляющую из текста все слова, содержащие "абв"
# - ['ПРИВЕТ', 'ЗАБВЕНИЕ', 'ПОКА'] -> ['ПРИВЕТ', 'ПОКА']

txt = input("Введите текст через пробел: ")
print(f"Исходный текст: {txt}")
find_txt = "АБВ"
lst = [i for i in txt.split() if find_txt not in i]
print(f'Результат: {" ".join(lst)}')
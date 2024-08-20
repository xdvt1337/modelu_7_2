def custom_write(file_name: str, strings: list):
    strings_positions = {}
    file = open(file_name, 'w', encoding='utf-8')
    a = 1
    for string in strings:
        position = file.tell()
        file.write(string + '\n')
        strings_positions[(a, position)] = string
        a += 1
    file.close()
    return strings_positions

# Проверка:

info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
        print(elem)
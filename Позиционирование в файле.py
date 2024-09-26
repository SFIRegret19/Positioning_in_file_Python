def custom_write(file_name, strings):
    string_positions = {}
    file = open(file_name, 'a', encoding='utf-8')
    counter = 1 # Т.к. нумерация начинается с 1
    for i in strings:
        tell = file.tell()
        if i.__eq__(strings[-1]):
            file.write(f'{i}')
            string_positions.update({(counter, tell): i})
        else:
            file.write(f'{i}\n')
            string_positions.update({(counter, tell): i})
        counter += 1
    file.close()

    return string_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
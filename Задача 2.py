#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
with open('RLE.txt', 'w', encoding='UTF-8') as file:
    file.write(input('Введите текст: '))
with open('RLE.txt', 'r') as file:
    my_text = file.readline()
    compression = my_text.split()
print(my_text)
def rle_encode(text):
    enconding = ''
    prev_char = ''
    count = 1
    if not text:
        return ''

    for char in text:
        if char != prev_char:
            if prev_char:
                enconding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        enconding += str(count) + prev_char
        return enconding

compression = rle_encode(my_text)
with open('Compression.txt', 'w', encoding='UTF-8') as file:
    file.write(f'{compression}')
print(compression)
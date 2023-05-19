"""Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковое значение
некоторой характеристики, и возвращают True, если это так. Если значение характеристики для разных объектов
отличается - то False. Для пустого набора объектов, функция должна возвращать True. Аргумент characteristic - это
функция, которая принимает объект и вычисляет его характеристику.
Ввод: 
values = [0, 2, 10, 6] 
if same_by(lambda x: x % 2, values):
print(‘same’)
else:
print(‘different’)
Вывод:
same"""

values = [0, 2, 10, 6] 
def same_by(characteristic, objects):
    result = [characteristic(object) for object in objects]
    for i in range(len(result)-1):
        if result[i] != result[i+1]:
            return False
    return True

if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')


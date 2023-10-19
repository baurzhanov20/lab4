def count_occurrences(input_tuple):
    element_count = {}

    for item in input_tuple:
        if isinstance(item, list):
            key = tuple(item)
        else:
            key = item

        if key in element_count:
            element_count[key] += 1
        else:
            element_count[key] = 1

    output_tuple = tuple((key, count) for key, count in element_count.items())

    return output_tuple

sample_input_1 = (55, 6, 777, 54, 6, 76, 7777, 1, 777, 6)
sample_input_2 = ('55', '6', '777', 54, 6, 7777, 9, 777, 6)
sample_input_3 = ((1, 2, 3), (['A', 'B']), (1, 2, 3), (['A']))

result_1 = count_occurrences(sample_input_1)
result_2 = count_occurrences(sample_input_2)
result_3 = count_occurrences(sample_input_3)

print("Sample Output 1:")
print("Elements and their occurrences:")
print(result_1)

print("\nSample Output 2:")
print("Elements and their occurrences:")
print(result_2)

print("\nSample Output 3:")
print("Elements and their occurrences:")
print(result_3)



#element_count = {}: Эта строка инициализирует пустой словарь с именем element_count. Словарь будет использоваться для хранения элементов из входного кортежа в качестве ключей и их соответствующих значений в качестве значений.
#Затем код выполняет итерацию по каждому элементу в input_tuple, используя цикл for.
#Внутри цикла:
#Он проверяет, является ли элемент списком, используя isinstance(элемент, список). Если это список, он преобразует список в кортеж с помощью tuple(item) и присваивает его переменной key. В противном случае он присваивает самому элементу значение key.
#Он проверяет, присутствует ли ключ уже в словаре element_count:
#Если это так, то он увеличивает количество для этого ключа.
#Если это не так, он добавляет ключ в словарь и устанавливает значение count равным 1.
#После обработки всех элементов во входном кортеже он создает новый кортеж с именем output_tuple, который содержит пары ключей и их количество, используя выражение генератора.
#Функция возвращает output_tuple, который содержит элементы из входного кортежа и их количество.
#Затем код предоставляет три примера входных кортежей, sample_input_1, sample_input_2 и sample_input_3, и использует функцию count_occurrences для подсчета вхождений элементов в каждом из них. Он печатает результаты для каждого выборочного входного кортежа.

#По сути, этот код подсчитывает вхождения элементов в кортеж, рассматривая как отдельные элементы, так и списки как элементы, и сохраняет результаты в новом кортеже. В нем демонстрируется, как подсчитывать и сообщать о появлении элементов в различных типах входных кортежей.


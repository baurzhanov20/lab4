set_A = {1, 2, 3, 4, 7}
set_B = {8, 7, 9, 4, 2, 0, 10}
set_C = {4, 0, 1}

for element in set_A.copy():
    if element in set_C:
        set_A.remove(element)
        set_B.add(element)
        set_C.remove(element)
        set_C.add(element)

print("Updated set_A:", set_A)
print("Updated set_B:", set_B)
print("Updated set_C:", set_C)



#set_A Установить = {1, 2, 3, 4, 7}: Эта строка определяет набор с именем set_A с элементами 1, 2, 3, 4 и 7.
#set_B Установить = {8, 7, 9, 4, 2, 0, 10}: Эта строка определяет другой набор, называемый set_B, с элементами 8, 7, 9, 4, 2, 0, и 10.
#set_C = {4, 0, 1}: Эта строка определяет третий набор, называемый set_C, с элементами 4, 0 и 1.
#Затем код вводит цикл for, который выполняет итерацию по копии set_A. Повторение по копии набора является хорошей практикой, позволяющей избежать изменения набора во время итерации.
#Внутри цикла:
#Он проверяет, присутствует ли элемент (элемент из копии set_A) также в set_C, используя элемент if в set_C: condition.
#Если элемент находится в set_C, он удаляет элемент из set_A с помощью set_A.remove(элемент). Эта операция удаляет общий элемент из set_A.
#Затем он добавляет тот же элемент в set_B, используя set_B.add(элемент). Эта операция добавляет удаленный элемент в set_B.
#Он удаляет элемент из set_C, используя set_C.remove(элемент), эффективно удаляя его из set_C.
#Он добавляет элемент обратно в set_C, используя set_C.add(элемент). Эта операция добавляет удаленный элемент обратно в set_C.
#После завершения цикла он печатает обновленные наборы:
#print("Обновленный set_A:", set_A) выводит измененный set_A.
#print("Обновленный set_B:", set_B) выводит измененный set_B.
#print("Обновленный set_C:", set_C) выводит измененный set_C.
#Код, по сути, выполняет серию операций для перемещения элементов между наборами на основе их присутствия в set_C. Он обновляет и печатает измененные наборы после этих операций.
import random

# список учеников
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
# отсортируем список учеников
students.sort()
# список предметов
classes = ['Математика', 'Русский язык', 'Информатика']
# пустой словарь с оценками по каждому ученику и предмету
students_marks = {}
# сгенерируем данные по оценкам:
# цикл по ученикам
for student in students:  # 1 итерация: student = 'Александра'
    students_marks[student] = {}  # 1 итерация: students_marks['Александра'] = {}
    # цикл по предметам
    for class_ in classes:  # 1 итерация: class_ = 'Математика'
        marks = [random.randint(1, 5) for i in range(3)]  # генерируем список из 3х случайных оценок
        students_marks[student][class_] = marks  # students_marks['Александра']['Математика'] = [5, 5, 5]
# выводим получившийся словарь с оценками:
for student in students:
    print(f'''{student}
            {students_marks[student]}''')
print('''
                Список команд:
                1. Добавить оценки ученика по предмету
                2. Вывести средний балл по всем предметам по каждому ученику
                3. Вывести все оценки по всем ученикам
                4. Выход из программы
                5. Удалить ученника.
                6. Изменить имя ученика.
                7. Изменить оценку.
                8. Удалить оценку.
                9. Удалить предмет.
                10. Изменить название предмета.
                11. Вывести все оценки по ученику.
                12. Вывод среднего балла по предметам по ученику.
                13. Добавить нового ученника.
                ''')

while True:
    students.sort()
    command = int(input("Введите команду: "))
    if command == 1:
        print('1. Добавить оценку ученика по предмету')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        # считываем название предмета
        class_ = input('Введите предмет: ')
        # считываем оценку
        mark = int(input('Введите оценку: '))
        # если данные введены верно
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            # добавляем новую оценку для ученика по предмету
            students_marks[student][class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
        # неверно введены название предмета или имя ученика
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
    elif command == 2:
        print('2. Вывести средний балл по всем предметам по каждому ученику')
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                # находим сумму оценок по предмету
                marks_sum = sum(students_marks[student][class_])
                # находим количество оценок по предмету
                marks_count = len(students_marks[student][class_])
                # выводим средний балл по предмету
                print(f'{class_} - {marks_sum // marks_count}')
            print()
    elif command == 3:
        print('3. Вывести все оценки по всем ученикам')
        # выводим словарь с оценками:
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()
    elif command == 4:
        print('4. Выход из программы')
        break
    elif command == 5:
        # удаление ученика
        while True:
            uchenik = input("Введите имя ученика, которого необходимо удалить, либо введите ""стоп"": ")
            if uchenik in students:
                students.remove(uchenik)
                del students_marks[uchenik]
                print("Ученик был успешно удален")
                break
            elif uchenik == "стоп":
                break
            else:
                print("Такого имени нет в списке")
                print()
    elif command == 6:
        # изменение ученика
        while True:
            uchenik1 = input("Введите имя ученика, которое необходимо изменить, либо введите ""стоп"": ")
            if uchenik1 in students:
                uchenik2 = input("Введите новое имя ученика: ")
                students[students.index(uchenik1)] = uchenik2
                students_marks[uchenik2] = students_marks.pop(uchenik1)
                # спасибо гуглу за подсказку
                print("Ученик был успешно изменен")
                print(students_marks)
                break
            elif uchenik1 == "стоп":
                break
            else:
                print("Такого имени нет в списке")
                print()
    elif command == 7:
        # изменение оценки
        while True:
            uchenik3 = input("Введите имя ученика, оценку которого необходимо изменить, либо введите ""стоп"": ")
            subject3 = input("Введите название предмета, по которому стоит оценка, либо введите ""стоп"": ")
            mark3 = int(input("Введите порядковый номер оценки, которую необходимо изменить: "))
            if uchenik3 in students and subject3 in classes:
                index1 = mark3 - 1
                students_marks[uchenik3][subject3][index1] = int(input("Введите новую оценку: "))
                print(f"Оценка успешно изменена,оценки {uchenik3} по {subject3}: ", students_marks[uchenik3][subject3])
                break
            elif uchenik3 == "стоп" or subject3 == "стоп":
                break
            else:
                print("Такого имени или предмета нет в списке")
                print()
    elif command == 8:
        # удаление ученика
        while True:
            uchenik4 = input("Введите имя ученика, оценку которого необходимо удалить, либо введите ""стоп"": ")
            subject4 = input("Введите название предмета, по которому стоит оценка, либо введите ""стоп"": ")
            mark4 = int(input("Введите порядковый номер оценки, которую необходимо удалить: "))
            if uchenik4 in students and subject4 in classes:
                index2 = mark4 - 1
                del students_marks[uchenik4][subject4][index2]
                print(f"Оценка успешно удалена,оценки {uchenik4} по {subject4}: ", students_marks[uchenik4][subject4])
                break
            elif uchenik4 == "стоп" or subject4 == "стоп":
                break
            else:
                print("Такого имени или предмета нет в списке")
                print()
    elif command == 9:
        # удаление предмета
        while True:
            subject5 = input("Введите название предмета, который необходимо удалить, либо введите ""стоп"": ")
            if subject5 in classes:
                classes.remove(subject5)
                print(f"Предмет {subject5} успешно удален")
                break
            elif subject5 == "стоп":
                break
            else:
                print("Такого предмета нет в списке")
                print()
    elif command == 10:
        # удаление предмета
        while True:
            subject6 = input("Введите название предмета, который необходимо изменить, либо введите ""стоп"": ")
            subject7 = input("Введите новое название предмета: ")
            if subject6 in classes:
                classes[classes.index(subject6)] = subject7
                print()
                print(f"Предмет {subject6} успешно переименован в {subject7}")
                print("Актуальный список предметов: ", classes)
                break
            elif subject6 == "стоп":
                break
            else:
                print("Такого предмета нет в списке")
                print()
    elif command == 11:
        while True:
            # Вывести все оценки по ученику
            uchenik5 = input("Введите имя ученика, либо введите ""стоп"": ")
            if uchenik5 in students:
                print(f"Оценки {uchenik5}: ", students_marks[uchenik5])
                break
            elif uchenik5 == "стоп":
                break
            else:
                print("Такого имени нет в списке")
                print()
    elif command == 12:
        while True:
            # Вывести средний бал по предметам по ученику
            uchenik6 = input("Введите имя ученика, либо введите ""стоп"": ")
            if uchenik6 in students:
                print()
                print(f"Средний бал {uchenik6} по предметам: ", )
                # цикл по предметам
                for class_ in classes:
                    # находим сумму оценок по предмету
                    marks_sum = sum(students_marks[uchenik6][class_])
                    # находим количество оценок по предмету
                    marks_count = len(students_marks[uchenik6][class_])
                    # выводим средний балл по предмету
                    print(f'{class_} - {marks_sum // marks_count}')
                break
            elif uchenik6 == "стоп":
                break
            else:
                print("Такого имени нет в списке")
                print()
    elif command == 13:
        while True:
            # Добавить нового ученика
            uchenik7 = input("Введите имя ученика, которого необходимо добавить: ")
            students.append(uchenik7)
            students.sort()
            print(f"Ученик {uchenik7} успешно добавлен, список учеников: ", students)
            break

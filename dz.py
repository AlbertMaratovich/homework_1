coworkers = ["Саня", "Маня", "Даня", "Таня", "Туся", "Пуся", "Вдуся"]
print(coworkers[0], coworkers[-1], sep=",")
print(coworkers[0::1])
print(coworkers[0::2])
print(len(coworkers))
new = input("Введите имя нового коллеги: ")
coworkers.append(new)
print("Новый список: ", coworkers[0::1], "Количество:", len(coworkers))
collega = input("Введите имя коллеги для проверки: ")
if collega in coworkers:
    print("Он работает с вами")
else:
    print("Он не работает с вами")
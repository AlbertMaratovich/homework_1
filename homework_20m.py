import json

with open("orders_july_2023.json", "r") as my_file:
    orders = json.load(my_file)
max_price = 0
max_order = ''
string1 = ""

# 1 Какой номер самого дорого заказа за июль?
for order_num, orders_data in orders.items():
    # получаем стоимость заказа
    price = orders_data['price']
    # если стоимость больше максимальной - запоминаем номер и стоимость заказа
    if price > max_price:
        max_order = order_num
        max_price = price
for order_num, orders_data in orders.items():
    if max_price == orders_data['price']:
        string1 = string1 + order_num + ", "
print(f'Номер(а) заказа с самой большой стоимостью в размере {max_price} тугриков: {string1}')

# 2 Какой номер заказа с самым большим количеством товаров?
max_count = 0
max_order2 = ''
string2 = ""
for order_num2, orders_data2 in orders.items():
    count_ = orders_data2["quantity"]
    if count_ > max_count:
        max_count = count_
        max_order2 = order_num2
for order_num22, orders_data22 in orders.items():
    if max_count == orders_data22['quantity']:
        string2 = string2 + order_num22 + ", "
print(f'Номер(а) заказа с самым большим количеством товаров ({max_count}шт.): {string2}')

# 3 В какой день в июле было сделано больше всего заказов?
days3 = []
dict3 = {}
counted3 = 0
date3 = ""
answer = ""
for orders_data3 in orders.values():
    date3 = orders_data3["date"]
    days3.append(date3)
sorted_days = set(days3)
for i in sorted_days:
    dict3[i] = days3.count(i)
for a, c in dict3.items():
    if c > counted3:
        counted3 = c
for d, m in dict3.items():
    if m == counted3:
        answer = answer + d + ", "
print(f'Даты заказов с самым большим количеством заказов,в размере {counted3} шт.: {answer}')
# 4 Какой пользователь сделал самое большое количество заказов за июль?
string4 = ""
for order_num44, orders_data44 in orders.items():
    if max_count == orders_data44['quantity']:
        string4 = string4 + str(orders_data44["user_id"]) + ", "
print(f'Юзеры с наибольшим количеством заказов, в размере {max_count} шт.: {string4}')

# 5 У какого пользователя самая большая суммарная стоимость заказов за июль?
dict5 = {}
counted5 = 0
users5 = ""
for orders_data5 in orders.values():
    user5 = orders_data5["user_id"]
    dict5[user5] = 0
for orders_data5 in orders.values():
    user5 = orders_data5["user_id"]
    dict5[user5] += orders_data5["price"]
for i in dict5.values():
    if counted5 < i:
        counted5 = i
for key, value in dict5.items():
    if counted5 == value:
        users5 = users5 + str(key) + ", "
print(f'Юзер(ы) с наибольшей стоимостью заказов, в размере {counted5} тугриков: {users5}')

# 6 Какая средняя стоимость заказа была в июле?
ordersum = 0
counter6 = 0
for order_num, orders_data in orders.items():
    counter6 += 1
    price = orders_data['price']
    ordersum += price
answer6 = round(ordersum/counter6)
print(f'Средняя стоимость заказа была {answer6} тугриков')

# 7 Какая средняя стоимость товаров в июле?
value7 = 0
for order_num, orders_data in orders.items():
    qua7 = orders_data['quantity']
    value7 += qua7
between7 = round(value7/counter6)
answer7 = round(answer6/between7)
print(f'Средняя стоимость товара была {answer7} тугриков')

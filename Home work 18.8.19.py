
N = int(input('Введите необходимое количество билетов: '))
All_price = []
for i in range(1, N+1):
    Age = int(input('Введите возраст посетителя: '))
    if 0 < Age < 18:
        Price = 0
    elif 18 <= Age < 25:
        Price = 990
    else:
        Price = 1390
    print(Price)
    All_price.append(Price)
print(All_price)
Total_price = sum(All_price)
print('Сумма заказа, руб: ', Total_price)
# Скидка на общий заказ свыше 3х билетов
if N>3:
    Total_price_skidka = Total_price*0.9
else:
    Total_price_skidka = Total_price
print('Итого к оплате, руб: ', Total_price_skidka)
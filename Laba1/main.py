height = float(input())
weight = float(input())
steps = int(input())
time = float(input())


step = height/4+0.37
distance = steps*step
V = distance/time
energy = 0.035*weight+(V**2/height)*0.029*weight
kkal = energy*time
print("Дистанция = ", distance, " сожженно ", kkal, " каллорий")
distancekm = distance/1000
print("Вы прошли ", distancekm, " км")
if distancekm<=2:
    print("Поднажми, осталось не так много")
elif distancekm<=4:
    print("Вы мололец! Продолжим тренировку?")
elif distancekm>4:
    print("Да! Вы проделали гигантскую работу!")
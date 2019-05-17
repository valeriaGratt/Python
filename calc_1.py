#Сделать калькулятор подсчёта Тангенса, синуса, косинуса, логарифма и факториала.
import math
print('Калькулятор')
while True:
	calc=int(input("""Выберете что вы хотите сделать/найти?
		1-Сложить
		2-Отнять
		3-Умножить
		4-Разделить
		5-Синус
		6-Косинус
		7-Тангенс
		8-Логорифм
		9-Факториал
		0-Завершение программы
		Ваш вариант-"""))

	if calc==1:
		a=int(input("Введите первое число "))
		b=int(input("Введите второе число "))
		c=a+b
		print('Ответ',c)
	elif calc==2:
		a=int(input("Введите первое число "))
		b=int(input("Введите второе число "))
		c=a-b
		print('Ответ',c)
	elif calc==3:
		a=int(input("Введите первое число "))
		b=int(input("Введите второе число "))
		c=a*b
		print('Ответ',c)
	elif calc==4:
		a=int(input("Введите первое число "))
		b=int(input("Введите второе число "))
		c=a/b
		print('Ответ',c)
	elif calc==5:
		vvod=int(input("Введите число "))
		c=math.sin(vvod)
		print('Ответ',c)
	elif calc==6:
		vvod=int(input("Введите число "))
		c=math.cos(vvod)
		print('Ответ',c)
	elif calc==7:
		vvod=int(input("Введите число "))
		c=math.tan(vvod)
		print('Ответ',c)
	elif calc==8:
		vvod=int(input("Введите число "))
		c=math.log(vvod)
		print('Ответ',c)
	elif calc==9:
		vvod=int(input("Введите число "))
		c=math.factorial(vvod)
		print('Ответ',c)
	elif calc==0:
		print('Благодарим за использование нашего калькулятора ')
		break
	
#Простая программа для проверки наличия выбранной пиццы в меню
my_pizza = ['marqarita', 'dyabola', 'sicialian', 'kalcone', 'marinara', 'kaprichoza', 'karbonara', 'salami', 'cezar']
x = str(input("Скажите пожалуйста, какую пиццу вы желаете заказать?: "))
if x in my_pizza:
    print("Ваш заказ будет выполнен в кратчайщие сроки!")
else:
    print("К сожалению, Вашего заказа нет в нашем меню")

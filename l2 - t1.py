age = int(input("Сколько тебе лет?  "))
if age < 7:
    print ("Тебе пора в детский сад")
elif 7 <= age < 18:
    print ("Скоро 1 сентября, надо в школу")
elif 18 <= age < 22:
    print ("Скоро начинается семестр, топай в ВУЗ")
elif 22 <= age < 65:
    print ("Работай давай")
else:
    print ("а вот и пенсия")
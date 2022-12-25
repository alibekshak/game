from function import go_notgo

while True:
    step = input("""
        Играть жми - 1
        Надоело жми - 2
        """ )
    if step == "1":
        name = input("Введите имя вашего друга, а я подумаю: ")
        rezalt = go_notgo(name)
        print(rezalt)
    elif step == "2":
        print("Наконец-то мы закончили, и так дел полно")
        break
    else:
        print("Только 1 или 2, гений")
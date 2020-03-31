# Create By Emre Çilekci//

is_alive = True
while is_alive:
    parola = input("Parolanız sadece rakamlardan oluşabilir ve içerisinde 0 olmamalıdır. \nLütfen Parola Giriniz: ")

    try:
        sayi = int(parola)

    except ValueError:
        print("Sadece Rakam Kullanılabilir")

    else:
        print("Üyelik Tamamlandı")
        is_alive = False

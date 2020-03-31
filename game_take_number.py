# Create By Emre Çilekci//

tahminsayı=42

is_alive = True
while is_alive:
    sayi=(int(input("1-100 arasında bir sayı tuttum.Bu sayıyı bilebilir misin?")))


    if sayi < 1 or sayi > 100:
        print("Lütfen 1-100 arasında sayı giriniz!!!")

    elif sayi < tahminsayı:
        print("Biraz daha büyük bir tahmin yapınız :)")

    elif sayi > tahminsayı:
        print("Biraz daha küçük bir tahmin yapınız :)")

    elif sayi == tahminsayı:
        print("Tebrikler Sayıyı Bildiniz :):):) \nBildiğiniz Sayı : {}".format(tahminsayı))
        is_alive = False

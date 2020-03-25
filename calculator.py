# Create By Emre Çilekci//
islem = """
(1) Topla
(2) Çıkar
"""
print(islem)
soru=input("Lütfen İşlem Seçiniz")
girdi = "İLK SAYI:  {} , İKİNCİ SAYI:  {}"

if soru not in  islem:
        print("Yanlış Seçim Yaptınız")

elif soru == "1":
    sayı1 = int(input("Toplama işlemi için ilk sayıyı girin:   "))
    sayı2 = int(input("Toplama işlemi için ikinci sayıyı girin:  "))

    print(girdi.format(sayı1, sayı2), "için toplama işleminin sonucu", (sayı1 + sayı2))

elif soru == "2":
    sayı1 = int(input("Çıkarma işlemi için ilk sayıyı girin:   "))
    sayı2 = int(input("Çıkarma işlemi için ikinci sayıyı girin:  "))

    print(girdi.format(sayı1,sayı2),"için çıkarma işleminin sonucu",(sayı1-sayı2))
not_user = "admin"
user_name = True

print ("Kullanıcı adı rakam içeremez ya da içerisinde \"admin\" kelimesi olamaz.")

while user_name :
    user_input = input("Lütfen kullanıcı adı giriniz:")
    try:
        if not_user == user_input :
            raise ValueError

        for i in user_input:
            if (i >='0' and i<='9'):
                raise TypeError

        print("Tebrikler! Kullanıcı adınız kaydedildi.")
        user_name = False

    except ValueError  :
        print("Kullanıcı adı \"admin\" olamaz.")

    except TypeError  :
        print("Kullanıcı Adında Rakam Olamaz")




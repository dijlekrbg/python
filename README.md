# python
#not uygulaması 

# 1-Menu
    # 1-Not Gir
    # 2- notları göster 
    # 3- Notları kayıt et.
    # 4-Çıkış
def not_gir():
    ad = input("ögrenci adi ") 
    soyad = input("öğrenci soyad ")
    not1 = input("not 1: ")
    not2 = input("not 2: ")
    not3 = input("not 3: ")

    with open("sinav_notları.txt","a",encoding="utf-8") as file:
        file.write(ad +' '+ soyad + ':' + not1 + ',' + not2 + ','+ not3 + '\n')



def not_oku():
    with open("sinav_notları.txt","r",encoding="utf-8") as file:
        for satir in file:
            print(satir)


def not_kayıt():
    pass 

while True:
    islem = input("1- not gir \n 2-Notları oku\n 3-Notları kayıt et \n 4-çıkış\n SEÇİM : ")

    if islem =="1":
        not_gir()

    elif islem =="2":
        not_oku()

    elif islem  =="3":
        not_kayıt()

    else:
        break    

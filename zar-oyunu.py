# import random
# while True:
#     x= input("zar atmak istiyor musunuz (e/h): ")
#     if x=="e":
#         zar = random.randint(1,6)
#         print("gelen sayı :",zar)

#     elif x=="h":
#         break

#     else:
#         print("hatalı giriş yaptınız. tekrar görüşmek üzere ")



import random 


def oyun():
    print(" ZAR ATMA OYUNUNA HOŞGELDİNİZ :)")
    while True:
        secim=kullaniciya_sor()

        if secim =="e":
            zar=zar_at()
            print( "gelen sayi :" , zar)

        elif secim =="h":
            print("tekrar görüşmk üzere . ")
            break
            
        else:
            print("hatalı seçim yaptınız. ")


def kullaniciya_sor():
    x=input("zar atmak istiyor musunuz (e/h): ")
    return x

def zar_at():
    return random.randint(1,6)

oyun()
def add(tel_rehberi):
    isim = input("İsim giriniz:")
    numara = input("Numara giriniz:")
    indis = ord(isim[0]) % 20
    count = 0
    for i in range(0, 20):
        if indis == i:
            for j in range(i, 20):
                if tel_rehberi[j] == 0:
                    tel_rehberi[j] = isim + "   " + numara
                    print("Eklendi\n")
                    count = 1
                    break
            if count == 0:
                for j in range(0, 20):
                    if tel_rehberi[j] == 0:
                        tel_rehberi[j] = isim + "   " + numara
                        print("Eklendi\n")
                        break
            if count == 0:
                print("Rehber dolu...\n")
            break


def silme(tel_rehberi):
    try:
        isim = input("Silinecek ismi giriniz:\n")
        indis = ord(isim[0]) % 20
        count = 0
        for i in range(0, 20):
            if indis == i:
                for j in range(i, 20):
                    if isim in tel_rehberi[j]:
                        tel_rehberi[j] = 0
                        print("Silindi\n")
                        count = 1
                        break
                if count == 0:
                    for j in range(0, 20):
                        if isim in tel_rehberi[j]:
                            tel_rehberi[j] = 0
                            print("Silindi\n")
                            break
                break
    except:
        print("Öyle biri yok")

def arama(tel_rehberi):
    try:
        isim = input("Aranacak isim nedir:")
        indis = ord(isim[0]) % 20
        count = 0
        for i in range(0, 20):
            if indis == i:
                for j in range(i, 20):
                    if isim in tel_rehberi[j]:
                        print(tel_rehberi[j])
                        count = 1
                        break
                if count == 0:
                    for j in range(0, i):
                        if isim in tel_rehberi[j]:
                            print(tel_rehberi[j])
                            break
                break
    except:
        print("Öyle biri yok")

tel_rehberi = []
for i in range(0, 20):
    tel_rehberi.append(0)
while 1:
    secim =int(input("Yapacağınız işlemin numarsını yazınız\n1)Ekleme\n2)Silme\n3)Arama\n4)Rehber\n5)Çıkış\n"))
    if secim == 1:
        add(tel_rehberi)
    elif secim == 2:
        silme(tel_rehberi)
    elif secim == 3:
        arama(tel_rehberi)
    elif secim == 4:
        print("Kişi   Numara")
        for i in tel_rehberi:
            if i != 0:
                print(i)

    elif secim == 5:
        break
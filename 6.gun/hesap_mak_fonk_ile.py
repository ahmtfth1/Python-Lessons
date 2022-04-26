
def giris_ekrani():
    print("Hangi işlem?")
    print("""1- Toplama
    2- Çıkarma

    Çıkmak için Ç harfine basınız.
    
    Seçim için sıra nosunu yazınız : 
    """)

def veri_girisi():
    sayilar = []
    while True:
        sayi = input("Sayıyı girin (Çıkmak için Ç'ye basın):")
        
        if sayi == "Ç":
            break

        sayi = int(sayi)

        sayilar.append(sayi)
    
    return sayilar

def toplama(a):
    # toplam = sayilar[0] + sayilar[1]
        toplam = 0
        # [30, 40, 60]
        for sayi in a:
            toplam = toplam + sayi

        print(f"Toplama sonucu : {toplam}")

def cikarma(b):
    fark = b[0]
        # 1, 2, 3, 4 .....
    for index in range(1,len(b)):
        fark = fark - b[index] 
    print(f"Çıkarma sonucu : {fark}")

def kullanici_secimi():
    k_secim = input()
    return k_secim


while True:
    
    # Kullanıcı ekranı yazdırma
    giris_ekrani()

    # kullanıcının seçim yapmasını sağlama
    secim = kullanici_secimi()

    # kullanıcının çıkış yapıp yapmadığını kontrol etme
    if secim == "Ç":
        break
    
    # Kullanıcının yanlış seçim yapıp yapmadığını kontrol etme
    if not (secim == "1" or secim == "2"):
        print("Yanlış giriş yaptın.")
        continue 
    
    # Kullanıcıdan verileri alma
    sayilar = veri_girisi()

    
    print(sayilar)

    # Kullanıcı 1 girmişse toplama fonk. çağır
    if secim == "1":
        toplama(sayilar)
    # Kullanıcı 2 girmişse cikarma fonk. çağır
    elif secim == "2":
        cikarma(sayilar)    

    else:
        print("Yanlış seçim yaptınız.")

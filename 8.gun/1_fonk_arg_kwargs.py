# parametre  olarak;
# *args -> birden fazla sıralı değişken fonk. gönderilebilir. args -> zorunlu, genel kullanım.
# *args -> veri türü tuple - demet
# **kwargs -> birden fazla key-value değeri gönderilebilir.

def toplama(*prt):
    print(prt)

toplama(5)
a = 4
b = 9
c = 10
toplama(a,b,c)
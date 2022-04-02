import os
import random
class Futbolcu():
    def __init__(self,ad,soyad,formano):
        self._ad=ad.capitalize()
        self._soyad=soyad.capitalize()
        self.formano=formano
        self.hız=random.randint(50,100)
        self.güç=random.randint(50,100)
        self.kondisyon=random.randint(50,100)
        self.şut=random.randint(50,100)
        self.dosyayayaz()
    def dosyayayaz(self):
        yol=os.path.join("C://Users//Eray/test")
        if os.path.exists(yol):
                print("Yol Bulundu Diğer İşlemlere Geçiliyor")
        else:
            print("Dosya Oluşturuluyor")
            os.mkdir("C://Users//Eray//test")
        os.chdir("C://Users//Eray//test")
        yaz=open("logfile.txt","a")
        yaz.write("{},{}\n".format(self._ad,self._soyad))
    def set_ad(self):
        isim=input("Girmek İstediğiniz Adı Yazınız")
        self._ad=isim
        print(self._ad)
    def set_soyad(self):
        isim = input("Girmek İstediğiniz Soyadı Yazınız:")
        self._soyad = isim
    def get_ad(self):
        print(self._ad)
    def get_soyad(self):
        print(self._soyad)



class Ortasaha(Futbolcu):
    mevki="Ortasaha"
    def __init__(self,_ad,_soyad,formano):
        super().__init__(_ad,_soyad,formano)
        self.uzuntop=random.randint(50,90)
        self.toplndirme=random.randint(50,90)
        self.uretkenlik=random.randint(50,90)

    def puanhesapla(self):
        self.puan=self.hız + self.güç + self.uzuntop + self.toplndirme + self.kondisyon + self.şut + self.uretkenlik
        print(self.puan)

    def yazdir(self):
        print("{},{},{},{},{}".format(self.formano,self._ad,self._soyad,self.mevki,self.puan))


class Defans(Futbolcu):
    mevki="Defans"
    def __init__(self,__ad,__soyad,formano):
        super().__init__(__ad,__soyad,formano)
        self.pozisyon=random.randint(60,100)
        self.kafa=random.randint(60,100)
        self.sıçrama=random.randint(60,100)
    def puanhesapla(self):
        self.puan=self.hız + self.güç + self.kafa + self.sıçrama + self.kondisyon + self.şut + self.pozisyon
    def yazdir(self):
        print("{},{},{},{},{}".format(self.formano,self._ad,self._soyad,self.mevki,self.puan))


class Forvet(Futbolcu):
    mevki="Forvet"
    def __init__(self,__ad,__soyad,formano,):
        super().__init__(__ad,__soyad,formano)
        self.bitiricilik=random.randint(70,100)
        self.ozelyetenek=random.randint(70,100)
        self.sondokunuş=random.randint(70,100)
    def puanhesapla(self):
            self.puan=self.hız + self.güç + self.bitiricilik + self.ozelyetenek + self.kondisyon + self.şut + self.sondokunuş
    def yazdir(self):
        print("{},{},{},{},{}".format(self.formano,self._ad,self._soyad,self.mevki,self.puan))

eray=Ortasaha("eray","dahan",19)
utku=Ortasaha("utku","dahan",34)
arda=Forvet("arda","sarıoğlu",28)
ercan=Forvet("ercan","yılmaz",10)
ali=Defans("ali","aldeniz",6)
mehmet=Defans("Mehmet","Aldeniz",16)

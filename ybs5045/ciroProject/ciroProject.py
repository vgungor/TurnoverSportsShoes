# -*- coding: utf-8 -*-
'''
Bir isletmenin 25 Ã§alisani bulunmaktadir. 
Buna gÃ¶re toplam ciro degerini hesaplayarak 
adambasi ciro degerini bulunuz. 

Ciro:Satis Miktari*Birim Satis Fiyati

Adambasi Ciro:Toplam Ciro/Toplam Ãalisan Sayisi

sm:Satis Miktari
bsf:Birim Satis Fiyati
tCiro:Toplam Ciro
tCalisan:Toplam Ãalisan Sayisi
aCiro:Adambasi Ciro
'''
import sys
#Çalışan için int harici değer girilmesi durumunda programdan çıkar
def tCalisanisInt():
    #farklı bir değer girilmez ise 25 veya girilen değer
    sayi = input("Çalisan sayisi giriniz (default=25): ")
    if(len(sayi)==0):
        sayi = 25
    try:
        sayi = float(sayi)
        #eğer sayısal değer girilmez ise programdan çıkar
    except ValueError:
        print("Lütfen bir sayı giriniz, KELİME değil")
        sys.exit()
    else:
        if((sayi % 1) == 0):
           return sayi
        else:
        #eğer negatif değer girilirse programdan çıkar
           print("Çalışan sayısı ondalık olamaz!!!")
           sys.exit()

#girilen değerin sayı olduğunu kontrol ediyor
def sayisalDegerAl(deger):
    try:
        sayi = float(input(f"{deger} giriniz: "))
    except ValueError:
        print("Lütfen bir sayı giriniz, KELİME değil")
    else:
        return sayi
	
#toplam ciro hesaplama
def ciro(sm,bsf):
    return sm*bsf

#adam basi ciro hesaplama
def adamBasiCiro(tCiro,tCalisan):
    return tCiro/tCalisan

def main():
    #Çalisan sayisi girdisi:
    tCalisan=tCalisanisInt()

    #Satis Miktari ve Birim Satis Fiyati:
    sm=sayisalDegerAl("Satis Miktari")
    bsf=sayisalDegerAl("Birim Satis Fiyati")

    print(f"Adam basi ciro: {adamBasiCiro(ciro(sm,bsf),tCalisan):0.2f} TL")

main()
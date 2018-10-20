'''
Bir isletmenin 25 çalisani bulunmaktadir. 
Buna göre toplam ciro degerini hesaplayarak 
adambasi ciro degerini bulunuz. 

Ciro:Satis Miktari*Birim Satis Fiyati

Adambasi Ciro:Toplam Ciro/Toplam Çalisan Sayisi

sm:Satis Miktari
bsf:Birim Satis Fiyati
tCiro:Toplam Ciro
tCalisan:Toplam Çalisan Sayisi
aCiro:Adambasi Ciro
'''
#girilen değerin integer olduğunu kontrol ediyor
def sayisalDegerAl(deger):
  sayi=input(f"{deger} giriniz: ")
  if(sayi.isnumeric()):
    sayi = int(sayi)
    if(sayi <= 0):
      print("Lütfen pozitif sayi giriniz!!")
    else:
      return sayi
  else:
    print("Lütfen bir sayi giriniz!!")
	
#toplam ciro hesaplama
def ciro(sm,bsf):
  return sm*bsf

#adam basi ciro hesaplama
def adamBasiCiro(tCiro,tCalisan):
  return tCiro/tCalisan

#Çalisan sayisi girdisi:
tCalisan=sayisalDegerAl("Çalisan sayisi")

#Satis Miktari ve Birim Satis Fiyati:
sm=sayisalDegerAl("Satis Miktari")
bsf=sayisalDegerAl("Birim Satis Fiyati")

print(f"Adam basi ciro: {adamBasiCiro(ciro(sm,bsf),tCalisan):0.2f} TL")
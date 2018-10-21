#global variable total çalışan
global tCalisan
tCalisan = 25

#toplam ciro hesaplama
def ciro(sm,bsf):
    return sm*bsf

#adam basi ciro hesaplama
def adamBasiCiro(tCiro,tCalisan):
    return tCiro/tCalisan

def main():
    
    #Çalisan sayisi girdisi:
    #tCalisan=float(input("Çalisan sayisi giriniz: "))

    #Satis Miktari ve Birim Satis Fiyati:
    sm=float(input("Satis Miktari giriniz: "))
    bsf=float(input("Birim Satis Fiyati giriniz: "))

    print(f"Adam basi ciro: {adamBasiCiro(ciro(sm,bsf),tCalisan):0.2f} TL")

main()
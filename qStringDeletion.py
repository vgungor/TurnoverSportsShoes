"""
degisken="QUERY_STRING='adi=can&soyadi=aydın&yas=35&il=izmir' "
bu post stringini dictionary'e çeviriniz. 
"""

def queryResult(query):
    #query içindeki "QUERY_STRING" kısmını sil, ' ' arası kalır
    dBase=query[(query.find("=")+1):].strip(" ").strip("'")
    #string türünü, dizi yapısına getir
    dBase=dBase.replace("&",",").replace("=",",")
    #string türünü listeye dönüştürdük
    dList=dBase.split(",")
    #
    qDict={}
    i=0
    while(len(dList)>i):
        qDict[dList[i]]=(dList[i+1])
        i+=2
    return qDict

#json ile çözüm - üzerinde çalıiılacak

def main():
    degisken="QUERY_STRING='adi=can&soyadi=aydın&yas=35&il=izmir&ilce=menemen&sokak=' "
    print(queryResult(degisken))

    
main()

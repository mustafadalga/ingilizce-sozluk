import json
from difflib import get_close_matches

data=json.load(open("data.json"))

def sozluk(k):
    k=k.lower()
    if k in data:
        return data[k]
    elif len(get_close_matches(k,data.keys()))>0:
        durum=input("%s'mi demek istediniz? Eğer evet ise evet,hayır ise hayır yazınız:" % get_close_matches(k,data.keys())[0])
        if durum=="evet":
            return data[get_close_matches(k,data.keys())[0]]
        elif durum=="hayır":
            return "Böyle bir kelime bulunamadı. Lütfen iki kez kontrol ediniz!"
        else:
            return "Aradığınız - %s - ile ilgili hiçbir arama sonucu mevcut değil." % durum
    else:
        return "Böyle bir kelime bulunamadı. Lütfen iki kez kontrol ediniz!"


kelime=input("Bir kelime giriniz:")
cevap=(sozluk(kelime))

if type(cevap)==list:
    for i in cevap:
        print(i)
else:
    print(cevap)

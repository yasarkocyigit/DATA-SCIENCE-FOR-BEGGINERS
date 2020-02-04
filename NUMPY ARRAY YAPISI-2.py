import numpy as np

arr=np.arange(25)

print(arr)#burada 25 dahil degil 0 ile 25 arasindaki degerleri vermis olacak

# RESHAPE KULLANIMI

print(arr.reshape(5,5))

#burada arr yi 5-5 bir matrise donusturmus olduk

#ama matrisin 5x5 lik olmasi lazim yani 5x4 yaparsak hata verecektir

"""
sonuc bu sekilde olacaktir=

[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]
 [20 21 22 23 24]]
"""

newArray = np.random.randint(1,100,10)# 1-100 arasinda 10 tane deger uret komutu

print(newArray)

print(newArray.max())# icindeki en buyuk degeri verir rastgele(yani her defasinda farkli en buyuk degeri doner)
print(newArray.min())# icindeki en kucuk degeri verir rastgele(yani her defasinda farkli en buyuk degeri doner)

print(newArray.sum())# sum ile icindeki butun degerlerin toplamini almis oluruz


print(newArray.mean()) # "mean" ile tum degerlerin ortalamisini bulabiliriz

""" YINE BURADA DA TUM KODLARI AYRI AYRI BASKA BIR PENCEREDE KARISMAMASI ACISINDAN DENENEBILIR. CIKTI DEGERLERIN DAHA IYI GORULMESI ACISINDAN"""


print(newArray.argmax())# burada da max. sayinin oldugu indexi verir
print(newArray.argmin())# burada da min. sayinin oldugu indexi verir


# DETERMINANT HESAPLAMA

detArray = np.random.randint(1,100,25)#burada 1-100 arasinda (100 dahil degil) 25 tane random deger olusturduk


print(detArray)#ciktisina baktik

detArray = detArray.reshape(5,5)#daha  sonra bunu 5 e 5 lik matrise donusturduk


print(detArray)#ciktisina baktik

print(np.linalg.det(detArray))#burada determinantini hesapladik


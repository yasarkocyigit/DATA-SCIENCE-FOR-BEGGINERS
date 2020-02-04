data_list = [1,2,3]

print(data_list)

import numpy as np

arr = np.array(data_list)

print(arr)

data_list2= [[10,20,30],[40,50,60],[70,80,90]]

arr2 = np.array(data_list2)

print(arr2)

#ya da daha onceden liste olusturmak zorunda degiliz direk listeyi icine de atabiliriz

arr3 = np.array([1,2,3,4,5,6,7,8,9,0])

print(arr3)

#genel olarak numpy listelerinin olusturulmasi bu sekilde

#liste icindeki elemanlara erismek icinse listelerde yaptigimiz gibi

print(arr3[0])#burada arr3 listesi icinde 0. index e erismik olduk

#arr2 matrisindeki 2 ye 2. indexi bulmak istedigimizde yani 2. indexin 2. indexi(o da 90 oluyor)
#gosterim bicimi

print(arr2[2,2,])#sonuc 90 olacaktir

#numpy uzerinde yine range metodunu kullanabiliriz

print(np.arange(10,20))#burada 10-20 arasindaki degerleri verir (20 dahil degil)

print(np.arange(0,99,3))#burada da 0-99 arasindaki degerleri 3 er atlayarak veriri

#10 tane ornek olarak 0 in depolandigi bir array yazmak istersek

print(np.zeros(10))

print(np.ones(10))#ya da 1 depolamak istersek "ones"

#bunlar tek boyutlu arrayler cok boyutlu matrisleride 0 ile doldurabiliriz

print(np.zeros((2,2)))#burada 2ye2 bir matris olustur icine de 0 degerlerini ver demis oluyoruz

print(np.zeros((3,6)))

"""BURADAKI ORNEKLERIN HER BIRINI AYRI BIR PENCEREDE KARISMAMASI ACISINDAN DENENEBILIR"""


# "linspace" kullanimi

print(np.linspace(0,100,5)) #burada 0-100 arasindaki degerleri 5 esit parcaya bolerek 5 tane deger olarak sakla demek
# 0  ile 100 de dahil


print(np.eye(6)) #burada 6 ya 6 bir matris olusturacak ve kosegenlerde hepsi 1 degerine sahip olacak
#yani bir tane birim matrisi olusturmus oluyoruz


print(np.random.randint(0,10))# 0 dahil 10 dahil degil
#burada 0 ile 10 arasinda rastgele degerler donecek
print(np.random.randint(10))#burada da 0 yazmasakta 0 yazmis gibi hareket edecek

print(np.random.randint(1,10,5))#burada 1-10 arasinda deger donsun ancak 5 tane deger donerek bunu bir tane array icinde sakla


print(np.random.randn(5))#burada sadece 0-5 arasinda degerler ortaya cikmayacak
#burada negatif degerlerde ortaya cikacak
#yani burada Gaussian distribution yapmis olduk

# [ 1.23090143 -0.28569486 -0.42070302 -0.73690302  0.98744533] bu sekilde ciktilar verecektir



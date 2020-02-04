import numpy as np


newArray = np.arange(1,21)

print(newArray)

#simdi bunu cok boyutlu matrise cevirmek istersek

newArray = newArray.reshape(5,4)

print(newArray)


print(newArray[0,0]) #yani burda matrsin 1. satirinin 1. sutunu

"""
[[ 1  2  3  4] ----> yani 1. satir 1. sutun = 1 olacaktir
 [ 5  6  7  8]
 [ 9 10 11 12]
 [13 14 15 16]
 [17 18 19 20]]
 
 """

#matrisin satirlarinin ilk degerini almak istiyor olalaim sadece

"""
[[ 1  2  3  4] ----> yani sadece burada 1,2 / 5,6 / 9,10 / 13,14 / 17,18 degerlerini almis olacagiz
 [ 5  6  7  8]
 [ 9 10 11 12]
 [13 14 15 16]
 [17 18 19 20]]
 
 """
print(newArray[:,:2])
#satirlarimin hepsini almak istiyorum onun icin en basta ":" kullaniyoruz
# daha sonra sutunlarin sadece ilk iki indexini almak icin ":2" kullaniyoruz

"""
[[ 1  2]
 [ 5  6]
 [ 9 10]  ---> ciktisini verecektir
 [13 14]
 [17 18]]
 
 """

print(newArray[:3,:3])
#burada ise satirlarin 0 1 ve 2.sini al sutunlardan da yine ayni sekilde  0 1 ve 2. yi al anlamina geliyor

"""
[[ 1  2  3]
 [ 5  6  7]  ---> ciktisini verir
 [ 9 10 11]]

"""

print(newArray[:2,:])
#burda da butun sutunlari aliyoruz ama sadece ilk iki satiri aliyoruz

"""
[[1 2 3 4]
 [5 6 7 8]]
"""

#ayni islemi su sekilde de yazabiliriz

print(newArray[:2])
#yani satirin yaninda butun sutunlari almak istiyoruz yazmazsak kendisi butun sutunlari otomatik dahil eder

"""
[[1 2 3 4]
 [5 6 7 8]]
"""


# ARRAY LERI FILTRELEME

arr=np.arange(1,11)

print(arr>3)
#burada 3 ten buyuk degerler icin True kucuk degerler icin False donecek

"""
[False False False  True  True  True  True  True  True  True]
"""

#filtrelemeyi su sekilde yapiyoruz

booleanArray = arr>3

print(arr[booleanArray])
#sadece true olan degerleri doner


"""[ 4  5  6  7  8  9 10]"""

print(arr[arr>5])
# 5 ten buyuk olan True degerleri doner

"""[ 6  7  8  9 10]"""
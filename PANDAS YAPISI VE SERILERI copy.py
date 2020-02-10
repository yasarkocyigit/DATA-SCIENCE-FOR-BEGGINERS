import numpy as np
import pandas as pd
# burada numpy da dahil ediyoruz cunku birbiriyle baglantili kullandigimiz yerler olacak


labels_list = ["mustafa" , "kemal" , "murat" , "tugce" , "tugba"]

data_list = [10,20,30,40,50]

# PANDAS SERILERINI BIR TANE INDEKS VE DEGERLERDEN OLUSAN ARRAY DIYEBILIIRIZ

print(pd.Series(data = data_list, index=labels_list))
"""
mustafa    10
kemal      20
murat      30 ----> ciktisini verir
tugce      40 
tugba      50
dtype: int64 --> burada datalarimizin hangi veritipinden oldugunu gorebiliyoruz

"""



print(pd.Series(data_list))

"""
0    10
1    20
2    30
3    40
4    50
dtype: int64

BURADA HERHANGIBIR INDEX VERMEDIGIMIZ ICIN 
OTOMATIK DEFAULT OLARAK 0,1,2,3,4. INDEKSLER OLARAK CIKAR

"""

npArray = np.array([10,20,30,40,50])

print(pd.Series(npArray))
#burada pandas icine bir array serisi verebiliriz
#burada print ettigimizde yine default olarak index karsiligini verir
"""
0    10
1    20
2    30
3    40
4    50
dtype: int64
"""

print(pd.Series(npArray,labels_list))
#burada herbir deger karsisine indeksi vermis olduk
"""
mustafa    10
kemal      20
murat      30
tugce      40
tugba      50
dtype: int64
"""

print(pd.Series(data=npArray, index=["A","B","C","D","E"]))
#burada da indexleri kendi istedgimiz gibi yazabiliriz

"""
A    10
B    20
C    30
D    40
E    50
dtype: int64

"""

dataDict = {"kadir":30, "kemal":80,"tugba":60}
#burada bir sozluk olusturup degerlerin karsiliklarini yazdik
print(pd.Series(dataDict))
#bu sozlugu pandas serisi olarak yazdirabiliriz
#asagidaki gibi vikti verir


"""
sozlukler sirali bir veritipi olmadigi icin karisik olarak cikmis oldu:


kadir    30
kemal    80
tugba    60
dtype: int64

"""

ser2017=pd.Series([5,10,14,20],["bugday","misir","kiraz","erik"])

print(ser2017)

ser2018=pd.Series([2,12,12,6],["bugday","misir","cilek","erik"])

print(ser2018)

#burada seriler arasinda " cilek " ve " kiraz "  farkli digerleri ayni

print(ser2018+ser2017)

"""
bugday     7.0
cilek      NaN
erik      26.0
kiraz      NaN
misir     22.0
dtype: float64

ORTAK OLMAYAN SERILERI TOPLAYAMAYACAGI ICIN "NOT A NUMBER" (NAN) HATASI ALMIS OLDUK


"""

total  = ser2018+ser2017

print(total["erik"])#burada degerlerden sadece erik  e karsilik geleni almak istedigimizi soyluyoruz

"""26.0"""  #cikti olarak sadece erik e karsilik gelen deger

print(total["cilek"])
#burada "nan" hatasinin ciktisini alacaktir




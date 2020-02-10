import numpy as np
import pandas as pd

arr = np.array([[10,20,np.nan],[5,np.nan,np.nan],[21,np.nan,10]])
#array olusturuyoruz once bir tane
#burada ornek olmasi acisindan icerisinde not a number (nan) degerler verdik

print(arr)

"""

[[10. 20. nan]
 [ 5. nan nan]
 [21. nan 10.]]

"""

#buradaki arrayden bir dataframe olusturuyoruz

df=pd.DataFrame(arr,index=["Index1","Index2","Index3"],columns=["Column1","Column2","Column3"])
#dataframe icin serilerin birlesmis hali diyebiliriz


print(df)

"""
        Column1  Column2  Column3
Index1     10.0     20.0      NaN
Index2      5.0      NaN      NaN
Index3     21.0      NaN     10.0

"""

#NaN olan verileri silmek icin "df.dropna" metodunu kullanabiliriz

df.dropna()
#burada axis=0 oldugu zaman index yani satira gore axis=1 oldugu zaman column yani sutuna gore siler
#yani burda index1,index2,index3 e bakicak NaN varmi yokmu?-varsa satirlari silecek

print(df.dropna())

"""
Columns: [Column1, Column2, Column3]
Index: []

silinmis hali bu sekilde olacaktir

burda index e gore silmis olduk NaN olan satirlari


"""

#column a gore de silebiliriz

df.dropna(axis=1)
#icine parametre olarak "axis=1" dersek bu sefer sutun yani column a gore siler
#icine birsey vermezsek otomatik "axis=0" olarak aldigi icin yani satirlari siler (indexleri yani)

print(df.dropna(axis=1))

"""
       Column1
Index1     10.0
Index2      5.0
Index3     21.0

-sadece column1 de NaN olmadigi icin digerleri silinmis oldu yani

"""

"""
ozet olarak
axis=0 oldugu zaman satirlari (indexleri) siler
axis=1 oldugu zaman sutunlari(columnlari) siler
"""

#eger bir satirda ki butun verileri silmek istemiyorsak "thresh" parametresini kullanabiliriz
#yani satirda 2 tane normal veri var bir tane NaN var diyelim o zaman silme tut komutu verebilirizi

df.dropna(thresh=2)
#yani burada satirda 2 tane sayi varsa tut silme demis oluyoruz

print(df.dropna(thresh=2))

"""
         Column1  Column2  Column3
Index1     10.0     20.0      NaN
Index3     21.0      NaN     10.0

goruldugu gibi burada  satirdaki 2 tane sayi olan yeryerler silinmemis duruyor icinde NaN olmasina ragmen
"""


# "NaN" degerleri yerine bir deger eklemek icin "fillna" yi kullanabiliriz(icinede deger vermemiz gerekiyor)
# fillna(value= buraya ne deger vermek istersek onu yaziyoruz)

print(df.fillna(value=1))
# 1 degerini verirsen NaN olan heryere 1 degeri gelir

"""
        Column1  Column2  Column3
Index1     10.0     20.0      1.0
Index2      5.0      1.0      1.0
Index3     21.0      1.0     10.0

burada NaN degeerleri yerine 1 gelmis oldu



"""

# NaN larin yerin dataframe icindeki tum sayilarini ortalamasini vermek istersek eger

#bunun icin once tum degerleri toplamamiz lazim ortalama degerini bulmak icin. yani first step degerleri toplamak

print(df.sum())

"""
Column1    36.0
Column2    20.0
Column3    10.0
dtype: float64

#sayilari toplayip birer seri haline donusturmus oldu
"""

# daha sonraki adim olarak gostermek istersek bu serileride toplayip tek bir sayi haline getirmek gerekiyor onun icinde:

print(df.sum().sum())
#yani burada yukaridaki seri haline getiriyor sonra o serileride toplayip tek bir seri haline getir komutunu vermis oluyoruz

"""
66.0

cikan sonuc tum sayilarin toplami 

"""

#next step olarakta NaN lari saymazsak 5 tane normal verimiz var toplam 9 veri var NaN lar iler beraber
# toplam veri sayisini bulmak icin "size" fonksiyonunu kullaniyoruz


print(df.size)

"""
9
#toplamda 9 veri var yani

"""

# kac tane NaN veri oldugunu bulmak icin ise "isnull" metodunu kullaniyoruz

print(df.isnull().sum())
#kac tane NaN oldugunu "isnull" ile buluyoruz kac tane oldugunu bulmak icin "sum" ile toplamina bakiyoruz

"""
Column1    0
Column2    2
Column3    2
dtype: int64

hangi columnda kac tane NaN var toplami

"""

print(df.isnull().sum().sum())#yine birtane daha "sum()" eklersek genel toplamini bulmus oluruzu
"""
4
yani genel toplam NaN sayisi

step by step bakarsak asamalara daha basit ve anlasilabilir olur...

"""

# 9 dan 4 u cikarirsek kac tane normal degerimiz oldgunu bulabiliriz
#bunun icin gerekli fonksiyon:

def calculateMean(df):
    totalSum = df.sum().sum()
    totalNum = df.size - df.isnull().sum().sum()

    return totalSum/totalNum

#yani burda total summary yani genel sayilarin toplamini bulduk
#daha sonra size dan yani kac tane veri varsa ordan(9 adet veri) toplam NaN veri sayisini cikarttik
#daha sonra toplami sayilarin toplam veri sayisina bolduk
#yani once sayilarin toplamini bulduk daha sonra genel ortalamayi aradigimiz icin buldugumuz toplami kac tane sayi varsa one bolduk


# simdi NaN larin yerine buldugumuz ortalamalari koymak icin "value=calculateMena" fonksiyonunu yazmamiz lazim

print(df.fillna(value=calculateMean(df)))

"""
        Column1  Column2  Column3
Index1     10.0     20.0     13.2
Index2      5.0     13.2     13.2
Index3     21.0     13.2     10.0

#burada gordugumuz gibi NaN larin yerine buldugumuz ortalamalari koymus olduk


"""

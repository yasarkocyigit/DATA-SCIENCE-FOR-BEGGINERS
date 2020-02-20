import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Column1":[1,2,3,4,5,6],
    "Column2":[100,100,200,300,300,100],
    "Column3":["Mustafa","Kamil","Emre","Ayşe","Murat","Zeynep"]
})

#modullerimizi dahil ettikten sonra dataframemiz olusturuyoruz

print(df)

"""
   Column1  Column2  Column3
0        1      100  Mustafa
1        2      100    Kamil
2        3      200     Emre
3        4      300     Ayşe
4        5      300    Murat
5        6      100   Zeynep

"""

# "head" kullanimi --> "head(n = 3)" burda " n=3 " dersek sadece ilk 3 satiri alir!
# anlasilacagi uzere "n" e verdigimiz degere gore alinacak satir sayisi belirlenir

print(df.head(n=3))

"""
 Column1  Column2  Column3
0        1      100  Mustafa
1        2      100    Kamil
2        3      200     Emre

goruldugu gibi burada sadece ilk 3 satir alinmis olur

"""

# dataframe icinde birbirini tekrar eden degerler var. Kac tane farkli deger var onu gormek icin:
# Kullanacagimiz fonksiyon: "unique"

print(df["Column2"].unique())

"""

[100 200 300]

"""

# "unique" degerlerin kac adet oldugunu bulmak icin ise: "nunique" fonksiyonu kullaniyoruz

print(df["Column2"].nunique())

"""
3
toplamda birbirinden farkli toplamda 3 adet unique yani essiz deger var

"""

# "value_count" fonksiyonu islevi

print(df["Column2"].value_counts())

"""
00    3
300    2
200    1
Name: Column2, dtype: int64

burada Column2 icinde hangi degerden kacar adet oldugunu verir bu fonksiyon

"""


# Ornekleri cesitlendirerek ogrenmek acisindan; "Column1" deki 4 ten buyuk degerleri ve 300 olan degerleri nasil buluruz
# burada dataframe filtreleme islemleri yapacagiz

print(df[df["Column1"] >=4])

"""
 Column1  Column2 Column3
3        4      300    Ayşe
4        5      300   Murat
5        6      100  Zeynep

burdq 4 ten buyuk degerler gelmis oldu

"""

#ayni zamanda son ornege ek olarak bir sart koyabiliriz ornegin "column2" de ki degerler de 300 olacak sekilde al diyebiliriz

print(df[(df["Column1"] > 2) & (df["Column2"] == 300)])

"""
 Column1  Column2 Column3
3        4      300    Ayşe
4        5      300   Murat

"""

# Column2 de ki butun degerleri bir sayi ile carpmak istersek eger:
# Column2 de ki her degerin uzerinde bir fonksiyon uygulamamiz lazim
# Bunun icinde pandas da ki "apply" fonksiyonunu kullanacagiz

def times3(x):
    return x * 3
#fonksiyonumuzu yazdik

print(times3(3))
"""
9

fonksiyon bu sekilde caliscak icine aldigi degeri 3 le carpar 

"""
#simdi bu fonksiyonu "Column2" deki herbir degere uygulamak icin yapmamiz gereken:

print(df["Column2"])

"""
0    100
1    100
2    200
3    300
4    300
5    100
Name: Column2, dtype: int64

normalde "column2" bu sekilde
"""
print(df["Column2"].apply(times3))

"""
0    300
1    300
2    600
3    900
4    900
5    300
Name: Column2, dtype: int64

"Column2" de ki butun degerleri goruldugu gibi 3 ile carpmis olduk

"""
# Eger ki "Column2" yi son halinde aldigi degerler ile guncellemek istersem:

df["Column2"] = df["Column2"].apply(times3)

print(df["Column2"])

"""
0    300
1    300
2    600
3    900
4    900
5    300
Name: Column2, dtype: int64

"Column2" yi yeni degerlerine guncellemis olduk yani artik 3 ile carpilmis haline guncellenmis oldu
"""

# "lambda" fonksiyonunu kullanarak islem yaoma( lambda : fonksiyon olusturmak icin kullaniyoruz "def" yerine tek satirda yazilabilir

print(df["Column2"].apply(lambda x : x*2))

"""
0     600
1     600
2    1200
3    1800
4    1800
5     600
Name: Column2, dtype: int64

Burada goruldugu gibi ayri bir fonksiyon olusturup eklemek yerine direkt "lambda" ile halledilebilir

"""

# "len" fonksiyonu ornek:

print(df["Column3"].apply(len))

"""
0    7
1    5
2    4
3    4
4    5
5    6
Name: Column3, dtype: int64

"column3" teki stringlerin uzunluklarini "len" ile tek tek gormus olduk
    
"""

# Columnlardan birini silmek istersek: "drop" fonksiyonunu kullaniyoruz

# columnlarin oldugu axis=1 olmasi lazim satirlarin oldugu axis=0

print(df.drop("Column3",axis=1))

"""
   Column1  Column2
0        1      300
1        2      300
2        3      600
3        4      900
4        5      900
5        6      300

Column3 burda silinmis oldu


"""

# eger burda silme islemini gerceklestirdikten sonra son haline guncellemek istersek "inplace = True" parametresini yazmamis lazim

print(df.drop("Column3",axis=1 , inplace=True))

#son haliyle "Column3" silinmis haline yani guncellenmis oldu dataframe


# dataframe uzerinde kac tane sutun yani calumn oldugunu bulmak icin:

print(df.columns)

"""

Index(['Column1', 'Column2'], dtype='object')

bu sekilde cikti verir
bunu ozellikle buyuk veri setlerinde kullaniyoruz

"""
# dataframe icinde kac tane satir yani index oldugunu bulmak icin

print(df.index)

"""

RangeIndex(start=0, stop=6, step=1)

"""
print(len(df.index))

"""
6 ciktisini verir

kac tane satir oldugunu "len" fonksiyonu ile bulabiliriz

"""

# indexlerini isimlerine bakmak icin:

print(df.index.names)

"""
burada: "[None]" ciktisini verecektir cunku dataframe e baktigimizda indexklerin isimleri olmadigini gorecegiz
"""

# bu arada dataframe in son haline bakalim

print(df)

"""
Column1  Column2
0        1      300
1        2      300
2        3      600
3        4      900
4        5      900
5        6      300

"""

# dataframe i column a gore "kucukten buyuge" dogru siralamak icin:

print(df.sort_values("Column2"))

"""
   Column1  Column2
0        1      300
1        2      300
5        6      300
2        3      600
3        4      900
4        5      900

"""

# "buyukten kucuge" dogru siralamak istersek eger: normalde "sort_value" fonks kullandigimizda icinde "ascending = True" default olarak verir
# "ascending = False" olarak degistirirsek eger o zaman buyukten kucuge dogru siralar

print(df.sort_values("Column2",ascending=False))

"""
   Column1  Column2
3        4      900
4        5      900
2        3      600
0        1      300
1        2      300
5        6      300

"""

#buraya kadar kullanilan operasyonlar "data mining" isinde cok kullanilan operasyonlar

# "PIVOT TABLE" mantigi
df2 = pd.DataFrame({
    "Ay" : ["Mart","Nisan","Mayıs","Mart","Nisan","Mayıs","Mart","Nisan","Mayıs"],
    "Şehir":["Ankara","Ankara","Ankara","İstanbul","İstanbul","İstanbul","İzmir","İzmir","İzmir"],
    "Nem":[10,25,50,21,67,80,30,70,75]
})

print(df2)

"""
    Ay     Şehir  Nem
0   Mart    Ankara   10
1  Nisan    Ankara   25
2  Mayıs    Ankara   50
3   Mart  İstanbul   21
4  Nisan  İstanbul   67
5  Mayıs  İstanbul   80
6   Mart     İzmir   30
7  Nisan     İzmir   70
8  Mayıs     İzmir   75

"""

# burada yapmak istedigimiz sey bu dataframe i daha guzel,toplu gostermek(yani programlama mantigida budur zaten kolaylastirmak)

#bu dataframe uzerinden bir pivot table olusturacagiz once

print(df2.pivot_table(index = "Şehir",columns ="Ay",values = "Nem"))

"""
Ay        Mart  Mayıs  Nisan
Şehir                       
Ankara      10     50     25
İstanbul    21     80     67
İzmir       30     75     70

yani buradaki amac dataframe i daha toplu duzgun bir hale getirmek
"""

# baska sekilde column ve indexlerin yerini degistirerekte yazmamiz mumkun

print(df2.pivot_table(index = "Ay",columns ="Şehir",values = "Nem"))

"""Şehir  Ankara  İstanbul  İzmir
Ay                            
Mart       10        21     30
Mayıs      50        80     75
Nisan      25        67     70

"""
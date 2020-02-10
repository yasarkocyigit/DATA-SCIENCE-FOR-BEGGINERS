# BURADA DATAFRAME DE KI GROUPBY SORGULARI CALISILMISTIR
# SQL TABLOLARINDA KI GROUPBY ILE BIREBIR AYNI!

import numpy as np
import pandas as pd

dataset = {
        "Departman":["Bilişim","İnsan Kaynakları","Üretim","Üretim","Bilişim","İnsan Kaynakları"],
        "Çalışan": ["Mustafa","Jale","Kadir","Zeynep","Murat","Ahmet"],
        "Maaş":[3000,3500,2500,4500,4000,2000]
        }

#dataset i dataframe'e ceviriyoruz burada
df = pd.DataFrame(dataset)

print(df)

"""
          Departman  Çalışan  Maaş
0           Bilişim  Mustafa  3000
1  İnsan Kaynakları     Jale  3500
2            Üretim    Kadir  2500
3            Üretim   Zeynep  4500
4           Bilişim    Murat  4000
5  İnsan Kaynakları    Ahmet  2000

#burada gordugumuz gibi dataset icinde verilenleri dataframe e cevirmis olduk
#tablo yapisi olusturduk yani
"""

# olusturdugumuz dataframe uzerinde "groupby" islemlerini yapmaya baslayabiliriz
# ornek olarak "groupby" ile departman uzerinde islemler yapalim

DepGroup = df.groupby("Departman")# "DepGroup" adli degiskene atadik
# "Departman" a gore islemk yapmak istedigimiz icin icine onu atiyoruz

print(DepGroup)

"""
<pandas.core.groupby.generic.DataFrameGroupBy object at 0x10cd1c208>

#calistirdigimizda bize boyle bir obje doner

#artik biz bu objenin uzerinde
-toplama
-min deger bulma
-ortalama deger bulma gibi islemleri yapabiliriz


"""

print(DepGroup.sum())

"""
                  Maaş
Departman             
Bilişim           7000
Üretim            7000
İnsan Kaynakları  5500

#burada departmanlara gore toplam maaslari bir araya getirmis olduk
"""

#islemi daha kisa yapabiliriz

print(df.groupby("Departman").sum())
#yine ayni sonucu verir

#sadece tek bir sektorun toplamini almak istersek


print(df.groupby("Departman").sum().loc["Bilişim"])
"""
Maaş    7000
Name: Bilişim, dtype: int64

#sadece bilisim departmaninin maaslarinin toplamini almis olduk

"""
# toplam cikan maas sonucunu integer e cevirip tek bir sayi olarak ciktisini alabiliriz
#yapmamiz gereken tek sey basina "int" yazmak

print(int(df.groupby("Departman").sum().loc["Bilişim"]))
"""
7000
#sadece 7000 olarak cikti verecektir

"""

# "sum" yerine "count" fonksiyonunu kullanirsak

print(df.groupby("Departman").count())
"""
                  Çalışan  Maaş
Departman                      
Bilişim                 2     2
Üretim                  2     2
İnsan Kaynakları        2     2

#bu sefer departmanlarda calisan sayisini bulmus oluyoruz

"""

# "max" degeri kullanimi

print(df.groupby("Departman").max())

"""
                  Çalışan  Maaş
Departman                      
Bilişim           Mustafa  4000
Üretim             Zeynep  4500
İnsan Kaynakları     Jale  3500

#departmanlarda calisan en fazla maas alanlarin ciktisini verir bu sekilde
#isim siralamsida sozlukteki buyukluge gore gerceklesiyor

"""

# "min" deger kullanimi

print(df.groupby("Departman").min())

"""
                Çalışan  Maaş
Departman                     
Bilişim            Murat  3000
Üretim             Kadir  2500
İnsan Kaynakları   Ahmet  2000

"""
# sadece maas degerlerini almak istersek yani isimleri almadan

print(df.groupby("Departman").min()["Maaş"])

"""
Departman
Bilişim             3000
Üretim              2500
İnsan Kaynakları    2000
Name: Maaş, dtype: int64

#sadece maaslari aldik isimler cikartilmis oldu

"""

#dataframe uzerinde adim adim giderek islemlerimizi gerceklestirebiliiriz yani
#ornegin sadece bilisim departmanini almak istersek


print(df.groupby("Departman").min()["Maaş"]["Bilişim"])

"""
3000

#sadece bilisim dep. ciktisini verir

"""

#toplam maaslarin ortalmasini bulmak istersek eger

print(df.groupby("Departman").mean())#buradaki "mean" ortalama bulmak icin kullandigimiz fonksiyon
"""

                  Maaş
Departman             
Bilişim           3500
Üretim            3500
İnsan Kaynakları  2750

#ortalama maaslarin ciktisi
"""
#yine adim adim istedgimiz gibi analiz edebiliriz

print(df.groupby("Departman").mean()["Maaş"]["İnsan Kaynakları"])

"""
2750

#burda sadece insan kaynaklari departmanini ortalama maasini almis olduk yani


"""

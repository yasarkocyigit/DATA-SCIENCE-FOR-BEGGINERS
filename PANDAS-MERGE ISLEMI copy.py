import numpy as np
import pandas as pd

# MERGE ISLEMINDE DATAFRAMELERIN ORTAK OLAN DEGERLERINI ALIP YENI BIR DATAFRAME OLUSTURMAK OLARAK TANIMLAYABILIRIZ
# YANI 2 KUME DUSUNUN ORTAK ELEMANLARINDAN OLUSTURDUGUMUZ KUME MERGE ISLEMIYLE ALIDIGIMIZ DEGERLERE ESIT

dataset1 = {
    "A" : ["A1","A2","A3"],
    "B" : ["B1","B2","B3"],
    "anahtar" : ["K1","K2","K3"]
}

dataset2 = {
    "X" : ["X1","X2","X3","X4"],
    "Y" : ["Y1","Y2","Y3","Y4"],
    "anahtar" : ["K1","K2","K5","K4"]
}

# datasetlerimizi yazdik sonrasinda dataframlerimizi olusturuyoruz

df1 = pd.DataFrame(dataset1,index = [1,2,3])

df2 = pd.DataFrame(dataset2,index = [1,2,3,4])



print(df1)

"""
    A   B anahtar
1  A1  B1      K1
2  A2  B2      K2
3  A3  B3      K3

"""

print(df2)

"""
   X   Y anahtar
1  X1  Y1      K1
2  X2  Y2      K2
3  X3  Y3      K5
4  X4  Y4      K4

"""

#BURADA birtane "anahtar" column una gore dataframeleri birlestirecegiz

# burada "anahtar" column una gore islem gerceklestirdigimiz zaMAN "K1" ve "K2" satirlarinin ortak oldugunu goruyoruz

"""
        FARK

JOIN : indexler uzerinden 
MERGE : columnlar uzerinden yapilir

"""

print(pd.merge(df1,df2,on = "anahtar"))
#burda onemli olana "on" parametresi "on" parametresine " anahtar" i yazdigimizda o zamana " anahtar kelimesine gore islem yapar

"""
   A   B anahtar   X   Y
0  A1  B1      K1  X1  Y1
1  A2  B2      K2  X2  Y2

Bu sekilde "anahtar kelimesine gore columnlari ortak alarak islem yapilir

"""
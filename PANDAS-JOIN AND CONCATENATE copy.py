import numpy as np
import pandas as pd

#concatenate: eklemek anlamina geliyor. 2 tane dataframe i istersek index e gore istersekte column a gore birbirine ekleyebiliyoruz

dataset1 = {
    "A": ["A1","A2","A3","A4"],
    "B":["B1","B2","B3","B4"],
    "C":["C1","C2","C3","C4"],
}

dataset2 = {
    "A": ["A5","A6","A7","A8"],
    "B":["B5","B6","B7","B8"],
    "C":["C5","C6","C7","C8"],
}

#simdi bu datasetlerden dataframe olusturuyoruyz

df1 = pd.DataFrame(dataset1,index = [1,2,3,4])
df2 = pd.DataFrame(dataset2,index = [5,6,7,8] )

print(df1)

"""
 A   B   C
1  A1  B1  C1
2  A2  B2  C2
3  A3  B3  C3
4  A4  B4  C4
"""

print(df2)

"""
  A   B   C
5  A5  B5  C5
6  A6  B6  C6
7  A7  B7  C7
8  A8  B8  C8

"""

#dataframe lerimizi olusturduk

#bunlari birbirine eklemek icin "concat" metodunu kullaniyoruz

print(pd.concat([df1,df2]))

"""
    A   B   C
1  A1  B1  C1
2  A2  B2  C2
3  A3  B3  C3
4  A4  B4  C4
5  A5  B5  C5
6  A6  B6  C6
7  A7  B7  C7
8  A8  B8  C8

#index lere gore topladigimiz zaman bu sekilde oluyor
# 2 tane dataframe i toplamak icin birbirlerine benzemesi lazim
#axis=0 a gore boyle toplama
"""

# column lari toplamak icin yine axis=1 yapmamiz lazim

print(pd.concat([df1,df2],axis=1))

"""
     A    B    C    A    B    C
1   A1   B1   C1  NaN  NaN  NaN
2   A2   B2   C2  NaN  NaN  NaN
3   A3   B3   C3  NaN  NaN  NaN
4   A4   B4   C4  NaN  NaN  NaN
5  NaN  NaN  NaN   A5   B5   C5
6  NaN  NaN  NaN   A6   B6   C6
7  NaN  NaN  NaN   A7   B7   C7
8  NaN  NaN  NaN   A8   B8   C8

#columnlari toplanmasi sonucunda toplanamayan degerler NaN olarak cikiyor


"""

# join metodu icin ornekler:

dataset3 = {
    "X" : ["X1","X2","X3","X4"],
    "Y" : ["Y1","Y2","Y3","Y4"],
    "anahtar" : ["K1","K2","K5","K4"]
}

#yine burda datasetimizi dataframe e ceviriyoruz

df3 = pd.DataFrame(dataset3,index= [1,2,3,4])

print(df3)

print(df3.join(df1))

"""
    X   Y anahtar   A   B   C
1  X1  Y1      K1  A1  B1  C1
2  X2  Y2      K2  A2  B2  C2
3  X3  Y3      K5  A3  B3  C3
4  X4  Y4      K4  A4  B4  C4


"""

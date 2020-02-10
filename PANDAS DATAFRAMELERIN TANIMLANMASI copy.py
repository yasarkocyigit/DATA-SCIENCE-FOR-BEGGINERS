import pandas as pd
import numpy as np

from numpy.random import randn

print(randn(3,3))#bruada negatif degerlerle beraber 3e3 bir matris olusturacak

"""
ornek:
[[ 3.05125875e-01  2.30795044e+00  7.93996435e-01]
 [-1.53363802e-01 -1.87714762e-01  7.93797135e-01]
 [-4.39728563e-01  1.91089607e-01 -2.02253836e-03]]
 """

#simdi burada 3e3 matristen birtane frame olusturacagiz


df = pd.DataFrame(data=randn(3,3),index=["A","B","C"],columns=["column1","column2","column3"])

print(df)

"""

   column1   column2   column3
A -1.501969 -1.272858 -0.265564
B  1.536454 -0.168669  0.083941
C -0.618879 -0.205629  0.867064

bu sekilde bir dataframe olusmus olur

aslinda serilerin birlesmis hali gibi dusunulebilir

yani A,B,C satirlari birer seri
column1,column2,column3 sutunlari ayri birer seri olarak kullanilabilir

"""
#ornek olarak column1 i almak istersek

print(df["column1"])

"""
A    1.492723
B    0.407823
C    0.592123
Name: column1, dtype: float64

burda sadece colum1 e denk gelen degerleri almis olduk
"""

print(type(df["column2"]))
#<class 'pandas.core.series.Series'>  burada turunun  seri oldugunu gorebiliriz

#yani sonuc olarak dataframe ler serilerin birlesimi olarak dusunulebilir


#BU SEFER A SATIRINI KULLANMAK ISTERSEK

print(df.loc["A"]) #burada loc location in kisaltilmasi


"""
column1   -0.953905
column2   -2.534302
column3    2.123128
Name: A, dtype: float64

column lar aslinda burda index gibi davrandi

type a bakarsak yine bunun seri oldugunu gorecegiz


"""


print(df[["column1","column2"]])

"""
burda da kucuk bir dataframe olusmus oldu 


    column1   column2
A -1.587557  1.081876
B  1.074711 -0.701565
C -1.114674  0.257387


"""

# DATAFRAME BIR TANE DAHA COLUMN EKLEMEK ISTERSEK

df["column4"] = pd.Series(randn(3),["A","B","C"])

print(df)

"""
burada yeni bir column un eklendigini goruruz

 
    column1   column2   column3   column4
A  0.241777  1.298464 -0.499235  1.585928
B  0.654612  2.820911 -1.472475 -0.416358
C -0.289617 -1.108525  0.453456 -0.062038

"""


df["column5"] = df["column1"] + df["column2"] + df["column3"]

print(df)

"""
column5 in yani 1-2-3 columnlarinin toplamini bu sekilde seriye ekleyebiliriz

 column1   column2   column3   column4   column5
A -0.983716  0.764547 -0.387030 -0.672593 -0.606199
B  0.431860 -0.382803  1.956575 -0.084792  2.005632
C -0.136474 -0.208077 -0.021431  0.413457 -0.365983

"""

# BIR TANE SUTUNU YA DA COLUMN I SILME

print(df.drop("column5" , axis=1))

"""
column5 i silindigini gormus oluruzu burda

 column1   column2   column3   column4
A  0.573660  0.493511 -0.099867 -0.138561
B -0.959622 -0.502691 -0.498539  1.156420
C -0.030925 -1.556798 -0.525098 -0.413382

"""

print(df)
#burada df yi tekrar yazdirirsak drop islemini yani silme islemini yaptiktan sonra
#drop ettigimiz column5 in tekrar geri geldgini goruruz

#icine bir parametre daha verirsek eger ancak kalici olarak silmis oluruz

print(df.drop("column5",axis=1,inplace=True))
#burada icine "inplace=True" parametresini verirsek bu sefer sil ve guncelle demis oluyoruz

print(df)

"""
burada silindigini gorebiliriz kalici olarakta guncellenmis olur

    column1   column2   column3   column4
A -0.174924 -0.159935 -0.106543  0.696225
B -0.022623  0.834390  0.449900 -1.901480
C  0.426884 -2.239874  0.856686  0.268647


"""

# INDEX E ERISMEK ICIN

print(df.loc["A"])
#sadece "A" satirindakileri almak icin


"""
column1   -0.817550
column2    1.117828
column3   -1.097090
column4   -1.565289
Name: A, dtype: float64

"""

print(df.iloc[0])
#burada yine ayni sonucu verir
"""
yine a satirini aldigimiz gibi ayni sonucu aldik burada


column1   -0.091171
column2    0.332072
column3    0.012015
column4    1.016859
Name: A, dtype: float64

"""


print(df.loc["A","column1"])
#burda da "A" endexine karsilik gelen column sutunundaki degeri almak istersek

"""
-1.8590818436924574

yine:
ornek:

df.loc["B","column2"]  desek bu seferde b nin column2 ye denk gelen degerini verir


"""
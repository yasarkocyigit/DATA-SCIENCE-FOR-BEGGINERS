import numpy as np
import pandas as pd

from numpy.random import randn


outerIndex =  ["Group1","Group1","Group1","Group2","Group2","Group","Group3","Group3","Group3"]


innerIndex = ["Index1","Index1","Index1","Index2","Index2","Index2","Index3","Index3","Index3"]


zip(outerIndex,innerIndex)
#burada zip fonksiyonunu kullaniyoruz
#ve zip fonksiyonunu daha sonra listeye cevirebiliriz


print(list(zip(outerIndex,innerIndex)))

"""

[('Group1', 'Index1'), ('Group1', 'Index1'), ('Group1', 'Index1'), ('Group2', 'Index2'), ('Group2', 'Index2'), ('Group', 'Index2'), ('Group3', 'Index3'), ('Group3', 'Index3'), ('Group3', 'Index3')]

"""

#dataframe i gruplamak istersek

hierarchy = list(zip(outerIndex,innerIndex))


hierarchy = pd.MultiIndex.from_tuples(hierarchy)

print(hierarchy)

"""
MultiIndex([('Group1', 'Index1'),
            ('Group1', 'Index1'),
            ('Group1', 'Index1'),
            ('Group2', 'Index2'),
            ('Group2', 'Index2'),
            ( 'Group', 'Index2'),
            ('Group3', 'Index3'),
            ('Group3', 'Index3'),
            ('Group3', 'Index3')],
           )
           
"""

df = pd.DataFrame(randn(9,3),hierarchy,columns=["column1","column2","column3"])

print(df)

"""
                column1   column2   column3
Group1 Index1  1.269333 -0.398785 -0.571607
       Index1 -0.400218 -0.538992 -0.906395
       Index1 -0.756547  0.201318  1.018360
Group2 Index2 -1.403767 -0.156331 -0.660266
       Index2  1.923512  0.648003  0.276761
Group  Index2  1.528844 -0.262915 -0.025348
Group3 Index3 -1.796768  2.367349  0.537825
       Index3 -0.595885 -1.379446  0.389105
       Index3  0.586776  1.258694 -1.312381
       
"""


print(df["column1"])

"""
SADECE COLUMN1 E AIT VERILERI ALIR


Group1  Index1    0.888592
        Index1    0.149276
        Index1   -0.062622
Group2  Index2   -0.130522
        Index2   -0.248451
Group   Index2    0.239760
Group3  Index3   -0.529793
        Index3    1.130778
        Index3    0.712903
Name: column1, dtype: float64
"""

print(df.loc["Group1"])

"""
BURADA DA SADECE GROUP1 ALINMIS OLDU
        column1   column2   column3
Index1 -0.675209  0.567387 -0.400552
Index1 -0.714443 -1.631250 -0.860060
Index1 -0.893227  0.274972  0.319853

"""

#YANI DATAFRAME ILE IHTIYACA GORE PARCALAYIP KULLANABILIRIZ VERILERI

print(df.loc[["Group1","Group2"]])

"""
SADECE GROUP1 VE GROUP2 ALINIR

               column1   column2   column3
Group1 Index1 -0.166519 -1.064305  1.522499
       Index1  2.532445  0.612128 -0.257651
       Index1  0.465853 -0.553955  0.142491
Group2 Index2  0.268160 -0.170358 -0.957564
       Index2 -0.221887 -0.610284  1.888540


"""

#GROUP1 IN ICINDEKI INDEX 1 IN DEGERLERINI BULMAK ISTERSEK EGER

print(df.loc["Group1"].loc["Index1"])

"""
yani sadece index1 i almis olduk

       column1   column2   column3
Index1  0.893492  1.563686  0.123854
Index1  0.480956  1.861047  1.081648
Index1  1.185695  0.354632  0.392441

"""

print(df.loc["Group1"].loc["Index1"]["column1"])

df.index.names= ["Groups","Index"]

print(df)


"""
burda grouplara Groups ismini indexlere de Index ismini vermis olduk


                column1   column2   column3
Groups Index                               
Group1 Index1 -0.973220  1.061227 -0.980360
       Index1 -0.297062 -1.447446  0.965287
       Index1 -0.483209 -0.057918  0.715275
Group2 Index2 -1.799557 -1.043056  0.248148
       Index2  1.357227  0.918505 -0.190696
Group  Index2  0.861682 -0.865498  0.177148
Group3 Index3 -1.622727  0.545117 -2.034281
       Index3 -1.084391 -0.130436 -1.968499
       Index3 -0.200170  0.328910 -1.009514


"""

print(df.xs("Group1"))

"""
     column1   column2   column3
Index                               
Index1 -0.401660 -0.004233 -1.454002
Index1  0.400219 -0.339027  1.815558
Index1 -0.028161 -2.415524 -0.344498


"""

print(df.xs("Group2").xs("Index2"))


print(df.xs("Index1",level= "Index"))
#burada sadece gruplarin index1 lerini almak istedigimizi soyluyoruz


import pandas as pd
import numpy as np

# you can use datas from kaggle as "csv"
# https://www.kaggle.com/datasnaek/youtube-new  this is the link that i am usind data from kaggle
# and when you download data which is "USvideos.csv" it must be in same folder
# "USvideos.csv" is in my folder already

dataset = pd.read_csv("USvideos.csv")

print(dataset)

# when you print out dataset its gonna look like this:

"""
          video_id  ...                                        description
0      2kyS6SvSYSE  ...  SHANTELL'S CHANNEL - https://www.youtube.com/s...
1      1ZAPwfrtAFY  ...  One year after the presidential election, John...
2      5qpjK5DgCt4  ...  WATCH MY PREVIOUS VIDEO ▶ \n\nSUBSCRIBE ► http...
3      puqaWrEC7tY  ...  Today we find out if Link is a Nickelback amat...
4      d380meD0W0M  ...  I know it's been a while since we did this sho...
...            ...  ...                                                ...
23357  pH7VfJDq7f4  ...  ...and other musings on thermal movement of la...
23358  hV-yHbbrKRA  ...  Visit Our Website! ▶ http://www.townsends.us/ ...
23359  CwKp6Xhy3_4  ...  Chris Young's Hangin' On from his #1 album Los...
23360  vQiiNGllGQo  ...  very wholesome stuff.\n\nThis video was taken ...
23361  2afSbqlp5HU  ...  The new marvel film Black Panther is set in th...

[23362 rows x 16 columns]

there are 23362 index and 16 columns in this dataset
"""

# if you wanna delete some things from this dataset you need to yous "drop" function and if you wanna delete from column you have to write "axis=1" alos
# if you wanna delete some things from index(row) you do not have to write anything because its axis=0 a=s default already

newdataset1 = dataset.drop(["video_id","trending_date"],axis = 1)

# when you look at "the newdataset1" you will see there is no "video_id","trending_date" anymore

print(newdataset1)

"""
                                                  title  ...                                        description
0                     WE WANT TO TALK ABOUT OUR MARRIAGE  ...  SHANTELL'S CHANNEL - https://www.youtube.com/s...
1      The Trump Presidency: Last Week Tonight with J...  ...  One year after the presidential election, John...
2      Racist Superman | Rudy Mancuso, King Bach & Le...  ...  WATCH MY PREVIOUS VIDEO ▶ \n\nSUBSCRIBE ► http...
3                       Nickelback Lyrics: Real or Fake?  ...  Today we find out if Link is a Nickelback amat...
4                               I Dare You: GOING BALD!?  ...  I know it's been a while since we did this sho...
...                                                  ...  ...                                                ...
23357                                Why Bridges Move...  ...  ...and other musings on thermal movement of la...
23358                      Macaroni - A Recipe From 1784  ...  Visit Our Website! ▶ http://www.townsends.us/ ...
23359                           Chris Young - Hangin' On  ...  Chris Young's Hangin' On from his #1 album Los...
23360      Elderly man making sure his dog won't get wet  ...  very wholesome stuff.\n\nThis video was taken ...
23361         How to speak like Black Panther - BBC News  ...  The new marvel film Black Panther is set in th...

[23362 rows x 14 columns]

as you can see "video_id","trending_date" columns dropped (deleted) from dataset
and there is 14 column after that

"""

# we created new dataset "as newdataset". if you wanna write this dataset as csv :

newdataset1.to_csv("UsVideosNew.csv")

# we created new csv in folder now wherever is your location

# if you do not wanna take indexes: the purpose is here making this code,app,programme(whatever) better and easier

newdataset1.to_csv("UsVideosNew.csv" , index=False)

print(newdataset1)

# that will be look better than last one

"""
                                                  title  ...                                        description
0                     WE WANT TO TALK ABOUT OUR MARRIAGE  ...  SHANTELL'S CHANNEL - https://www.youtube.com/s...
1      The Trump Presidency: Last Week Tonight with J...  ...  One year after the presidential election, John...
2      Racist Superman | Rudy Mancuso, King Bach & Le...  ...  WATCH MY PREVIOUS VIDEO ▶ \n\nSUBSCRIBE ► http...
3                       Nickelback Lyrics: Real or Fake?  ...  Today we find out if Link is a Nickelback amat...
4                               I Dare You: GOING BALD!?  ...  I know it's been a while since we did this sho...
...                                                  ...  ...                                                ...
23357                                Why Bridges Move...  ...  ...and other musings on thermal movement of la...
23358                      Macaroni - A Recipe From 1784  ...  Visit Our Website! ▶ http://www.townsends.us/ ...
23359                           Chris Young - Hangin' On  ...  Chris Young's Hangin' On from his #1 album Los...
23360      Elderly man making sure his dog won't get wet  ...  very wholesome stuff.\n\nThis video was taken ...
23361         How to speak like Black Panther - BBC News  ...  The new marvel film Black Panther is set in th...

[23362 rows x 14 columns]

"""
# reading writing on excel files with pandas: using "read_excel"
# excel file mustbe in same folder

excelset = pd.read_excel("excelfile.xlsx")

print(excelset)

"""
 Unnamed: 0  Column1  Column2  Column3  Column4
0     Index1       10       50       90      130
1     Index2       20       60      100      140
2     Index3       30       70      110      150
3     Index4       40       80      120      160

"""

# if you wanna add column on this dataset which is excelset

excelset["Column5"] = [170,180,190,200]

print(excelset)

"""
 Unnamed: 0  Column1  Column2  Column3  Column4  Column5
0     Index1       10       50       90      130      170
1     Index2       20       60      100      140      180
2     Index3       30       70      110      150      190
3     Index4       40       80      120      160      200

column will be added already 

"""

# if you wanna save this excel file to different(another excel file) excel file: using "to_excel"

excelset.to_excel("excelfilenew.xlsx")

"""
Unnamed: 0  Column1  Column2  Column3  Column4  Column5
0     Index1       10       50       90      130      170
1     Index2       20       60      100      140      180
2     Index3       30       70      110      150      190
3     Index4       40       80      120      160      200

it will be saved as new excel file right in the location folder

"""

# If you wanna take dataset from website: using "read_html"

new = pd.read_html("http://www.contextures.com/xlSampleData01.html",header = 0)

print(new)
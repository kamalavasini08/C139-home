# -*- coding: utf-8 -*-
"""C139 HOME.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12-uiwCUYh9iqNPdy_aTdBx3DrijrPEus
"""

!pip install kaggle

#Upload kaggle.json here, that we downloaded in C-138

from google.colab import files
files.upload()

!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/

!chmod 600 ~/.kaggle/kaggle.json

!kaggle datasets download -d gspmoreira/articles-sharing-reading-from-cit-deskdrop

!ls

!unzip articles-sharing-reading-from-cit-deskdrop.zip

!ls

import pandas as pd 
import numpy as np 

df1=pd.read_csv('shared_articles.csv')
df2=pd.read_csv('users_interactions.csv')

df1.head()

df2.head()

"""# Demographic Filtering"""

df1 = df1[df1['eventType'] == 'CONTENT SHARED']
df1.head()

df2.shape

df1.shape

def find_total_events(df1_row):
  total_likes = df2[(df2["contentId"] == df1_row["contentId"]) & (df2["eventType"] == "LIKE")].shape[0]
  total_views = df2[(df2["contentId"] == df1_row["contentId"]) & (df2["eventType"] == "VIEW")].shape[0]
  total_bookmarks = df2[(df2["contentId"] == df1_row["contentId"]) & (df2["eventType"] == "BOOKMARK")].shape[0]
  total_follows = df2[(df2["contentId"] == df1_row["contentId"]) & (df2["eventType"] == "FOLLOW")].shape[0]
  total_comments = df2[(df2["contentId"] == df1_row["contentId"]) & (df2["eventType"] == "COMMENT CREATED")].shape[0]
  return total_likes + total_views + total_bookmarks + total_follows + total_comments

df1["total_events"] = df1.apply(find_total_events, axis=1)

df1.head()

df1 = df1.sort_values(['total_events'], ascending=[False])

df1.head()


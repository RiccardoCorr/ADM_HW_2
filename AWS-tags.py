#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import json
from collections import Counter
import time


# we import the data
file_pathl = "list.json"
ch_size = 100
dfls = []

with open(file_pathl, "r") as filel:
    
    for chl in pd.read_json(filel, lines = True, chunksize = ch_size):
        chl = chl[[
"tags"]]
        dfls.append(chl)

dfl = pd.concat(dfls, ignore_index=True)



# In[4]:


# We start the time AFTER importing the file
start_time = time.time()

# We sum every time we found a tag
tags = dfl['tags'].apply(lambda x: x if isinstance(x, list) else []).sum()

#Count
tagc = Counter(tags)

#We make a list with the top 5 tags
topt = tagc.most_common(5)

# we print the tags
for tag, count in topt:
    print(f"{tag}\t{count}")

#we end the time
end_time = time.time()

#print the time
print('the running time of the script is', f"{end_time-start_time:.4f}", 'sec')


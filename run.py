# Sajad Vahedi
# First feature of the project

import csv
import pandas as pd
import numpy as np

 
with open('tweets.json', 'rb') as f:
    data = f.readlines()
    data = map(lambda x: x.rstrip(), data)
    data_json_stri = "[" + ','.join(data) + "]"
    data_df = pd.read_json(data_json_stri)
   
    with open('ft1.csv', 'wb') as s:
        writer = csv.writer(s, delimiter = '\t', lineterminator = '\n',)
        for i in xrange (0,int(data_df.tail(1).index.values)):

 
            try:
                tw = data_df['text'][i].encode("utf-8")
            except IndexError:
                tw = 'null'
            except TypeError:
                tw = 'null'
            except AttributeError:
                tw = 'null'
 
            try: 
                twttim = str(data_df['created_at'][i])
            except IndexError:
                twttim = 'null'
            except TypeError:
                twttim = 'null'
 
 
 
            twttime = twttim.encode('utf-8') 
            writer.writerow([tw, " (timestamp: "+ twttime +")"])
            
            
            


import os
import re
import requests
import pdb
import pandas as pd
import time
from pathlib import Path


for ele in os.listdir('Page'):
    if ele == 'liste_complete.html' :
        pass
    else:
        path_folder=os.path.join('Page',ele,)
        path_file = os.path.join(path_folder,'page.html')
        with open(path_file,'r',encoding='utf8') as output:
            contenu=output.read()

        if contenu.find('reports#detailedcardmep')== -1:
            pass
        else:
            pattern='/meps/fr/(.*?)/main-activities/reports#detailedcardmep'
            Result=re.findall(pattern,contenu)
            my_header= {'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:137.0) Gecko/20100101 Firefox/137.0'}
            url='https://www.europarl.europa.eu/meps/fr/{}/main-activities/reports#detailedcardmep'.format(Result[0])
            print(url)
            
            req=requests.get(url,headers=my_header,timeout=10)
            content=req.text
            path=os.path.join(path_folder,'rapport.html')
            with open (path,'w',encoding='utf-8') as output:
                output.write(content)
       
        


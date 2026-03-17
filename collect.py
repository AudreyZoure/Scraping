import os
import requests
import re
import time


my_header= {'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:137.0) Gecko/20100101 Firefox/137.0'}
url='https://www.europarl.europa.eu/meps/fr/full-list/all'
req = requests.get(url,headers=my_header,timeout=10)
if req.status_code!=200:
    print('pb status code')
else:
    contenu=req.text
    path_file=os.path.join('Page','liste_complete.html') 
    with open (path_file,'w', encoding= 'utf8') as output:
        output.write(contenu)




pattern = r'<a href="https://www.europarl.europa.eu/meps/fr/(.*?)" itemprop="url" class="erpl_member-list-item-content mb-3 t-y-block">'
result = re.findall(pattern, contenu)

for n, ele in enumerate(result):
    if n == 20:
        break
    print(ele)
    path_folder = os.path.join('Page', ele)
    os.makedirs(path_folder, exist_ok=True)

    deputy_url = f'https://www.europarl.europa.eu/meps/fr/{ele}'
    try:
        req = requests.get(deputy_url, headers=my_header, timeout=10)
        deputy_content = req.text

        path_file = os.path.join('Page',ele,'page.html')
        with open(path_file, 'w', encoding='utf8') as output:
            output.write(deputy_content)

        print(f" Page du député {ele} sauvegardée.")

    except requests.exceptions.RequestException as e:
        print(f" Erreur lors de la récupération de {deputy_url} : {e}")
        continue

    time.sleep(0.5)
00

    
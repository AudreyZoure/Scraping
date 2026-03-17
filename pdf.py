# import os
# import re
# import requests 
# import pdb

# for ele in os.listdir('Page'):
  
#   path_file = os. path.join('Page',ele, 'rapport.html')
#   if os.path.exists(path_file):
#      with open(path_file,'r',encoding='utf-8') as output:
#          content = output.read()
#          '''
#          "https://www.europarl.europa.eu/doceo/document/A-10-2025-0045_FR.pdf"
#          '''
#          pattern ='https://www.europarl.europa.eu/doceo/document/(.*?)\.pdf'

#          result = re.findall (pattern, content)
#          print(result)
#          print(ele,len(result))
#          for i,url in enumerate (result):
#              path=os.path.join('Page',ele,'Rapport_{}.pdf'.format(i))
#              reponse=requests.get(url)
#              with open(path,'wb') as f:
#                f.write(reponse.content)
        


import os
import re
import requests

for ele in os.listdir('Page'):
    path_file = os.path.join('Page', ele, 'rapport.html')
    if os.path.exists(path_file):
        with open(path_file, 'r', encoding='utf-8') as output:
            content = output.read()
            pattern = r'https://www.europarl.europa.eu/doceo/document/(.*?)\.pdf'
            result = re.findall(pattern, content)
            print(result)
            print(ele, len(result))
            for i, url in enumerate(result):
                pdf_url = f"https://www.europarl.europa.eu/doceo/document/{url}.pdf"
                pdf_path = os.path.join('Page', ele, f'Rapport_{i}.pdf')
                response = requests.get(pdf_url)
                response.raise_for_status()
                os.makedirs(os.path.dirname(pdf_path), exist_ok=True)
                with open(pdf_path, 'wb') as f:
                    f.write(response.content)
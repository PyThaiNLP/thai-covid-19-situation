import glob,os
from pathlib import Path
import pdfbox
import wget
import requests
import tqdm
from archivenow import archivenow
from bs4 import BeautifulSoup
import re

with open("listpdf.txt","r") as f:
  list_file = [i.strip() for i in f.readlines()]

oldpage = requests.get("https://ddc.moph.go.th/viralpneumonia/situation_more.php", timeout=30)
page = requests.get("https://ddc.moph.go.th/viralpneumonia/situation.php", timeout=30)
soup= BeautifulSoup(oldpage.text, "html.parser")
links = soup.find_all('a', href=re.compile(r'(\.pdf)'))
for i in links:
  check = 'file/situation/' in i['href']
  temp = i['href'].replace('file/situation/','')
  if temp not in list_file and check:
    list_file.append(temp)

soup= BeautifulSoup(page.text, "html.parser")
links = soup.find_all('a', href=re.compile(r'(\.pdf)'))
for i in links:
  check = 'file/situation/' in i['href']
  temp = i['href'].replace('file/situation/','')
  if temp not in list_file and check:
    list_file.append(temp)

txt = ""
i= 0
while i < len(list_file):
  txt += list_file[i]
  if i != len(list_file) -1:
    txt += '\n'
  i+=1

with open("listpdf.txt","w") as f:
  f.write(txt)

with open("listpdf.txt","r",encoding="utf-8-sig") as f:
    listpdf_temp = [i.strip() for i in f.readlines()]
#print("Save to web.archive.org")
#for i in tqdm.tqdm(listpdf_temp):
#    archivenow.push("https://ddc.moph.go.th/viralpneumonia/file/situation/"+i,"ia")

pdf = pdfbox.PDFBox()
p = os.path.join(".", "pdf")
txt = os.path.join(".", "text")
#print(p)
listfile = [Path(i).name for i in list(glob.glob(p+"/*.pdf"))]
listpdf = [i for i in listpdf_temp if i not in listfile]
#print(listfile)
#print(listpdf)

for i in listpdf:
    try:
        wget.download("https://ddc.moph.go.th/viralpneumonia/file/situation/"+i,out=p)
        pdf.extract_text(os.path.join(p,i),output_path = os.path.join(txt,i.replace("pdf","txt")))
    except Exception as e:
        print("File : " + str(i))
        print(e)

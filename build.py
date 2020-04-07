import glob,os
from pathlib import Path
import pdfbox
import wget
import requests
import tqdm
from archivenow import archivenow

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
        pdf.extract_text(os.path.join(p,i),output_path=os.path.join(txt,i.replace("pdf","txt")))
    except Exception as e:
        print(e)
from archivenow import archivenow
from tqdm import tqdm

with open("listpdf.txt","r",encoding="utf-8-sig") as f:
    listpdf_temp = [i.strip() for i in f.readlines()]
print("Save to web.archive.org")
for i in tqdm.tqdm(listpdf_temp):
	print(archivenow.push("https://ddc.moph.go.th/viralpneumonia/file/situation/"+i,"ia"))
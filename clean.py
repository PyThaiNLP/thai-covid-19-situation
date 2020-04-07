import glob,os
from pythainlp.util import normalize
p = os.path.join(".", "text")
listfile = [i for i in list(glob.glob(p+"/*.txt"))]
def readfile(path):
    with open(path, "r", encoding="utf-8-sig") as f:
        return f.read()

def writefile(path, data):
    with open(path, "w", encoding="utf-8") as f:
        f.write(data)

def clean(data):
    return data.replace("","์").replace("","่").replace("","้").replace("","ี").replace("","๋").replace("","้").replace("","่").replace("","ิ").replace("","ื").replace("","ั").replace("","๊").replace("","ั")

listdata = [normalize(clean(readfile(i))) for i in listfile]

for i,file in enumerate(listfile):
    writefile(file, listdata[i])
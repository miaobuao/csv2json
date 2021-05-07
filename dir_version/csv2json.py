# 这个程序是对目录内拓展名为csv的文件进行批量转化
import json
import re,os

def is_csv(name):
    if re.match("[cC][sS][vV]",name.split('.')[1]):
        return True
    return False

def csv2json(csv_path,out_path):
    lines=[]
    res=[]
    with open(csv_path,"r",encoding="utf8") as csv:
        lines=csv.readlines()

    lines=[i.split(',')[0:-1] for i in lines]
    col_name=lines[0]
    lines=lines[1:]
    for line in lines:
        cell={}
        for i in range(len(line)):
            cell[col_name[i]]=float(line[i])
        res.append(cell)

    with open(out_path,"w+",encoding="utf8") as f:
        f.write(json.dumps(res,indent=1,ensure_ascii=False))

path="./Python/" #保存了csv文件的文件夹,请用 / 替换 \ 

for i in os.walk(path):
    for fs in i[2]:
        fullname=i[0]+"/"+fs
        if(is_csv(fs)):
            csv2json(fullname,fs.split('.')[0]+".json")

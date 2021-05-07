import json

lines=[]
res=[]

csv_path=input("CSV的路径：")
out_path=input("输出的json文件的路径：")
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

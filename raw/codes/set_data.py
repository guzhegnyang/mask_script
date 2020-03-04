# coding = utf-8
import json
data = list()
data.append(input("药店名："))
data.append(input("姓名："))
data.append(input("手机号："))
data.append(input("身份证号："))
with open("../data.txt", 'w') as f:
    f.write(json.dumps(data))
#["利群金鼎广场", "谷正阳", "13355426001", "370203200003248619"]
StringList1=["hello","hi","hi","ghana","hi","hello"]
MStringList1=[]
for i in StringList1:
    if StringList1.count(i)>=2 and i not in MStringList1:
        MStringList1.append(i)
print(MStringList1)
#a
for i in MStringList1:
    if StringList1.count(i)%2==0:
        print(i,"occurs even no. of times")
    else:
        print(i,"occurs odd no. of times")
#b
s=set(StringList1)
StringList1=list(s)
print(StringList1)
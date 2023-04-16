salaries_and_tenures = [(83000, 8.7), (88000, 8.1), (48000, 0.7), (76000, 6), (
    69000, 6.5), (76000, 7.5), (60000, 2.5), (83000, 10), (48000, 1.9), (63000, 4.2)]

gr1=[]
gr2=[]
gr3=[]

for s,t in salaries_and_tenures:
    if t<2:
        print(f"({s},{t}) belongs to less than 2 tenure")
        gr1.append(s)
    if t>=2 and t<=5:
        print(f"({s},{t}) belongs to bet 2 and 5 tenure")
        gr2.append(s)
    if t>5:
        print(f"({s},{t}) belongs to more than 5 tenure")
        gr3.append(s)
a1=sum(gr1)/len(gr1)
a2=sum(gr2)/len(gr2)
a3=sum(gr3)/len(gr3)
print("Averege salary of Group 1 is: ",a1)
print("Averege salary of Group 2 is: ",a2)
print("Averege salary of Group 3 is: ",a3)

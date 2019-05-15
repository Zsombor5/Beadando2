import string
def feladat3():
    x=input("Szó: ")
    lst=[]
    while True:
        while x!="0":
            if x not in lst:
                lst.append(x)
            elif x in lst:
                c = input("új szó: ")
                while True:
                    if c=="0":
                        return lst
                    if c not in lst:
                        lst.append(c)
                        break
                    if c in lst:
                        c=input("új szó: ")
                    continue
            x = input("Szó: ")
        break
    return lst


def torol(lst):
    szamok=[]
    jelek=[]
    for i in lst:
        for j in string.punctuation:
            if j in i:
                jelek.append(j)
    for z in jelek:
        if z in lst:
            lst.remove(z)
    for i in lst:
        if i.isdigit():
            szamok.append(i)
    for c in szamok:
        if c in lst:
            lst.remove(c)
    print(lst)



def fel(lst):
    n=len(lst)
    for i in range(n):
        for j in range(i+1,n):
            if lst[i][0]>lst[j][0]:
                lst[i],lst[j]=lst[j],lst[i]
            if lst[i][0]==lst[j][0]:
                if len(lst[i])<len(lst[j]):
                    lst[i],lst[j]=lst[j],lst[i]
            if lst[i][0]==lst[j][0] and len(lst[i])==len(lst[j]):
                lst[i],lst[j]=lst[j],lst[i]
    return lst
a=feladat3()
torol(a)
print("Az eredeti lista: {}".format(a))
print("A rendezett lista: {}".format(fel(a)))

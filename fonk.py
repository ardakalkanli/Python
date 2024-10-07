def asallik(x:int):
    bools= True
    if x==2:
        return bools
    for i in range(2,x):
        if x % i==0:
            bools= False
            return bools
        else: return bools
    
print(asallik(2))
def toplam(m):
    toplam1=0
    for a in m:
        toplam1+=a
    return toplam1

def ortlama(x: list):
    skurt = toplam(x) / len(x)
    return skurt
k=[5,6,7,8,9,10]
print(ortlama([5,5,6,7,8]))
lst = [5, 6, 11, 8, 0, 2, 3]

def finMinNumber(lst):
    min_value = min(lst)  
    return [i for i in lst if i == min_value]

numberList = finMinNumber(lst)
print(f"min number :",numberList)

def minNumber(x:list):
    k=[5,6,7,4,3,5,67,8]
    a=k.sort()
    b=x[0]      #return a[0]
    return a[0]

print(minNumber())
a={4,"rt","ert","tuı",1,3,7,"tg"}
b={6,4,3,6,8,2,7,4,"rt","tg","tgyth","ghdg"}

def same(m:set,n:set):
    samethings=set()
    for i in m:
        for k in n:
            if i ==k:
                samethings.add(i)
            else:pass
    return samethings

print(same(a,b))
def fibo(a:int):
    m=1
    n=1
    if a==1 or a==2:
        return 1
    else: return fibo(a-1) + fibo(a-2)
dizi=[]
for i in range(10):
    dizi.append(fibo(i+1))
print(dizi)


alfabe = "abcçdefgğhıijklmnoöprsştuüvyzxwq abc"
tence = input("tence:")
pastence = ""


for i in tence:
    if i in alfabe:
        newkey = alfabe.index(i) +3
        pastence += alfabe[newkey]
    else: print("küçük harflerle, işaretsiz yaz")
    
    break

print(pastence)
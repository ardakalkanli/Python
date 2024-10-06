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

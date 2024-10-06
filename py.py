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

   
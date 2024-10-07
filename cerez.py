book_list= ["keloğlan","balıkadam","at kafası","yarrra beni", "keloğlan", "juliet","yarrra bizi", "yarrra beni", "sokak köpeği"]
kolay= set(book_list)
while True:
    print("""
    [1]kitap sayısı
    [2]kitap çıkar
    [Q]bas sktir git
    """)
    choose=input("seç birini:")
    if choose == "1":
        adet_var= {i: book_list.count(i) for i in set(book_list)}
        print(adet_var)
    elif choose=="2":
        secim=input("kimi çıkarcaz:")
        if secim in book_list:
            if int(book_list.count(secim)) > 1:
                kaldi= int(book_list.count(secim))
                print(f"burada {secim} kitabından {kaldi-1} tane kaldı")
            elif int(book_list.count(secim))==1:                
                print(f"{secim} kalmadı")
        else:print("burda yok")
    elif choose =="q" or choose=="Q":
        break
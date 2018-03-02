while True:
    data=input("Sifrelenicek Kodu Giriniz : ")
    islem=str(input("Sifrelemek Icin e Cozmek Icın d ye basınız :"))
    if islem =="e":
        cipher=[]
        for c in range(len(data)):
            cipher.append(chr(ord(data[c])+3))
        print(''.join(cipher))
    elif islem=="d" :
        cipher = []
        for c in range(len(data)):
            cipher.append(chr(ord(data[c]) - 3))
        print(''.join(cipher))
    else:
        print("Hatali Islem Sectiniz...")
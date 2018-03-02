while True:
    data = input("Lutfen Kredi Karti Numarasi Giriniz :")
    if len(data)==16 or len(data)==15:
        sum=0
        for c in range(len(data)):
            if c % 2 == 0:
                sum=(int(data[c])*2)
            else :
                sum=(int(data[c]))

        if sum % 10 == 0:
            print("Kredi Karti Gecerlidir.")
        else :
            print("Kredi Karti Gecerli Degildir.")
    elif len(data) != 16 or len(data) != 15:
        print("Gecersiz Kredi Karti Numarasi.")
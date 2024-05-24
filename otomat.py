language = input("Whic language do you prefer?(Tr/En) / Hangi dili tercih edersiniz?(tr/en)").lower()
print(language)

totalFee = 0


if language == "en":
    print("""
    SNACKS
    ---------------------
    1-PİZZA(90₺)
    2-HAMBURGER(60₺)
    3-CHİCKEN(80₺)
    4-COOKİE(30₺)
    5-CAKE(50₺)
    6-CHİPS(30₺)
    7-POPCORN(30₺)
          
    DRİNKS
    ---------------------
    8-COFFE(40₺)
    9-LEMONADE(20₺)
    10-MİLK(30₺)
    11-JUCİE(20₺)
    12-TEA(10₺)
    13-AYRAN(20₺)
    14-WATER(5₺)      
          
    """)

    while True:
        prefer = input("What would you like?: ")
        many = int(input("How many would you like?: "))
        if prefer == "1":
            totalFee += many *90
        elif prefer == "2":
            totalFee += many*60
        elif prefer == "3":
            totalFee += many*80
        elif prefer == "4":
            totalFee += many*30
        elif prefer == "5":
            totalFee += many*50
        elif prefer == "6":
            totalFee += many*30
        elif prefer == "7":
            totalFee += many*30
        elif prefer == "8":
            totalFee += many*40
        elif prefer == "9":
            totalFee += many*20
        elif prefer == "10":
            totalFee += many*30
        elif prefer == "11":
            totalFee += many*20
        elif prefer == "12":
            totalFee += many*10
        elif prefer == "13":
            totalFee += many*20
        elif prefer == "14":
            totalFee += many*5
            
        question = input("Whould like anythink else?:(y/n)  ").lower()
        if question == "n":
            print("Total price: ",totalFee,"₺")
            print("See you again..")
            break



elif language == "tr":
    print("""
    ATIŞTIRMALIKLAR
    ---------------------
    1-PİZZA(90₺)
    2-KÖFTE(60₺)
    3-TAVUK(80₺)
    4-KURABİYE(30₺)
    5-KEK(50₺)
    6-KIZARMIŞ PATATES(30₺)
    7-PATLAMIŞ MISIR(30₺)
          
    İÇECEKLER
    ---------------------
    8-KAHVE(40₺)
    9-LİMONATA(20₺)
    10-SÜT(30₺)
    11-MEYVE SUYU(20₺)
    12-ÇAY(10₺)
    13-AYRAN(20₺)
    14-SU(5₺)      
          
    """)

    while True:
        prefer = input("Ne istersiniz?: ")
        many = int(input("Kaç adet istersiniz?: "))
        if prefer == "1":
            totalFee += many *90
        elif prefer == "2":
            totalFee += many*60
        elif prefer == "3":
            totalFee += many*80
        elif prefer == "4":
            totalFee += many*30
        elif prefer == "5":
            totalFee += many*50
        elif prefer == "6":
            totalFee += many*30
        elif prefer == "7":
            totalFee += many*30
        elif prefer == "8":
            totalFee += many*40
        elif prefer == "9":
            totalFee += many*20
        elif prefer == "10":
            totalFee += many*30
        elif prefer == "11":
            totalFee += many*20
        elif prefer == "12":
            totalFee += many*10
        elif prefer == "13":
            totalFee += many*20
        elif prefer == "14":
            totalFee += many*5
            
        question = input("Başka birşey istermisiniz?:(e/h)  ").lower()
        if question == "h":
            print("Toplam hesap: ",totalFee,"₺")
            print("Tekrar görüşmek üzere..")
            break

else:
    print("You should prefer the language / Dil tercih etmelisin")

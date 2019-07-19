
try:
    while True:
        print("======= ADAM ASMACA OYUNU=======\n"
              "             V 1.0")

        kelime = "Ankara"

        kelime = kelime.upper()

        tahminler = []

        hata = []

        deneme = 6

        resim = ["""
           +---+
           |   |
               |
               |
               |
               |
        --------""", """
           +---+
           |   |
           O   |
               |
               |
               |
        --------""", """
           +---+
           |   |
           O   |
           |   |
               |
               |
        --------""", """
           +---+
           |   |
           O   |
          /|   |
               |
               |
        --------""", """
           +---+
           |   |
           O   |
          /|  |
               |
               |
        --------""", """
           +---+
           |   |
           O   |
          /|  |
          /    |
               |
        --------""", """
           +---+
           |   |
           O   |
          /|  |
          /   |
               |
        --------"""]

        resim.reverse()

        while deneme > 0 :
            print(resim[deneme])
            tabela = ""
            for harf in kelime:
                if harf in tahminler:
                    tabela = tabela+harf

                else:
                    tabela = tabela + " _ "

            if tabela == kelime:
                print(" Tebrikler ! KElimeyi Dogru Bildiniz..")
                break

            print("Kelimeyi Tahmin Ediniz", tabela)

            print(deneme, " canin kaldi. ")

            tahmin = input(" KElimeyi tahmin icin bir harf giriniz : ")

            tahmin = tahmin.upper()

            if tahmin==kelime:
                print("Tebrikler ! Harfi Dogru Bildiniz..")
                break


            if tahmin in tahminler or tahmin in hata:
                print("{} harfi daha once soylendi. Bir hakkiniz yandi. Lutfen baska bir harf giriniz".format(tahmin))


            if deneme >= len(resim):
                print("Kaybettiniz!nn")
                break


            elif tahmin in kelime:
                print(" Dogru tahmin ettiniz ! ")

                tahminler.append(tahmin)


            else:
                print("Yanlis. Kelimede bu harf Yok !")

                hata.append(tahmin)

                deneme = deneme-1


        if deneme==0:
            print("Hic hakkiniz kalmadi malesef bilemediniz ! \n"
                  "KElime : ",kelime)

        print("Oyundan cikmak istiyorsaniz q ya basiniz, devam etmek icin baska bir tusa basiniz")
        devam = input(": ")
        devam = devam.upper()

        if devam=="q":
            break
        else:
            continue

except ValueError:
    print("Lutfen Talimatlara Uygun HAreket Ediniz !")

except type:
    print("Lutfen Talimatlara Uygun HAreket Ediniz !")



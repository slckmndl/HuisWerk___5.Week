
print(" ===================================\n"
      "        Gorevler Uygulamasi\n"
      " ===================================")

giris = """

Yapilacak Islemi Seciniz : 

1. Gorev Ekleme 
2. Gorev Silme
3. Yapilanlar Listesini Goruntule
4. Yapilacaklar Listesini Goruntule

Secim : \n """


yapilacaklar_listesi = []

yapilanlar_listesi = []


anahtar=0



while True:

      try:

            islem = int(input(giris))

            if islem==1:
                  gorev = input(" Gorevi Yaziniz (cikmak icin q ye basiniz) : ")

                  if gorev=="q":
                        break

                  else:
                        yapilacaklar_listesi.append(gorev)

            elif islem==2:
                  print(yapilacaklar_listesi)

                  # if len(yapilacaklar_listesi)<=0:
                  #       print("fsfsdfsdfs")




                  sil = int(input("Kacinci gorevi silmek IStiyorsunuz ? : "))

                  del yapilacaklar_listesi[sil-1]
                  print(yapilacaklar_listesi)


            elif islem == 3:
                  print(yapilanlar_listesi)

            elif islem==4:
                  print("Yapilacaklar Listesi\n\n", yapilacaklar_listesi,"\n")


                  a = input("Tamamlandi olarak degistirmek istediginiz gorev numarasini "
                            "giriniz (Yapilacaklar Listesini Bosaltmak icin 'Sil' Yaziniz..)")

                  if a=="Sil":
                        yapilacaklar_listesi=yapilacaklar_listesi.clear()
                        print(yapilacaklar_listesi)

                  a = int(a)

                  yapilanlar_listesi = yapilacaklar_listesi.pop(a-1)

            elif islem>4 or islem<=0:
                  print("Lutfen 1 ile 4 arasinda bir rakam giriniz")







      except ValueError:
            print("Lutfen Seceneklerden Birini Rakam Olarak Giriniz ! ")

      except TypeError:
            print("Numara Istenilen yere harf, harf istenilen yere rakam girilmez ! ")



















print ("vitejte v python academii")
           
print("začiname gitovat")

list1 = [1, 2, 3, 4, 5]

print ("hello world")

print ("zěmna řadku")






print("ahoj engeto")

mesta = ["Praha", "Vídeň" ,"Olomouc", "svitavy", "Zlín", "Ostrava"]
ceny = (150, 200, 120, 120, 100, 100)
cara = "=" * 35
nabídka = """
1 - Praha   | 150,-Kč
2 - Vídeń   | 200,-Kč
3 - Olomouc | 120,-Kč
4 - Svitavy | 120,-Kč
5 - Zlín    | 100,-Kč
6 - Ostrava | 100,-Kč
 """

print("Vitejte u naší aplikace Destinatio")
print(cara)
print(nabídka)
print(cara)
print(cara, nabídka, end='')
print(cara)
destinace = input("45")
jmeno = input("JMENO")
prijmeni = input("PRIJMENI")
email = input("E-MAIL")

print(cara)
cilova_stanice = mesta[int(destinace) - 1]
finalni_cena = ceny[int(destinace) -1]

print(cilova_stanice)
print(finalni_cena, ",-Kč", sep='')

print(cara)

print("Cestujici", jmeno, prijmeni)
print("Ciclová destinace:", cilova_stanice)
print("Cena jízdného:", finalni_cena, ",-Kč")
print("jízdenku jsme odeslali na e-mail", email)
clear

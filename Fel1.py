def feladat(n):
    if n>1000:
        print("A megadott szám nagyobb mint 1000")
        quit()
    if n<0:
        print("A megadott szám kisebb mint 0")
        quit()
    lst1 = []
    lst2 = []
    for i in range(0, n):
        lst1.append(str(i))
    a = len(lst1)
    for i in lst1:
        if "1" in i or "2" in i or "3" in i or "5" in i or "6" in i or "8" in i or "9" in i:
            a -= 1
        elif "0" in i or "4" in i or "7" in i:
            lst2.append(i)
    print(lst2)
    return a
try:
    n = int(input("Adjon meg egy egész számot (0-1000): "))
    print("{} db ilyen szám van".format(feladat(n)))
except ValueError:
        print("Nem egész szám a megadott érték")


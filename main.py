buyurtmalar = []
while True:
    mahsulot = input("Mahsulot nomini kiriting (tugatish uchun stop): ")
    if mahsulot == "stop":
        break
    else:
        buyurtmalar.append(mahsulot)
print("Buyurtmalar ro'yxati:")
print(buyurtmalar)
mahsulotlar = {}
while True:
    nom = input("Mahsulot nomini kiriting (stop - tugatish): ")
    if nom == "stop":
        break
    else:
        narx = input("Mahsulot narxini kiriting: ")
        mahsulotlar[nom] = narx
print("E-bozor mahsulotlari va narxlari:")
print(mahsulotlar)
mahsulotlar = {}
while True:
    nom = input("E-bozor mahsulotini kiriting (stop - tugatish): ")
    if nom == "stop":
        break
    else:
        narx = input("Mahsulot narxini kiriting: ")
        mahsulotlar[nom] = narx
buyurtmalar = []
while True:
    nom = input("Buyurtma mahsulotini kiriting (stop - tugatish): ")
    if nom == "stop":
        break
    else:
        buyurtmalar.append(nom)

for mahsulot in buyurtmalar:
    if mahsulot in mahsulotlar:
        print(mahsulot, "-", mahsulotlar[mahsulot], "so'm")
    else:
        print(mahsulot, "- Bizda bu mahsulot mavjud emas")


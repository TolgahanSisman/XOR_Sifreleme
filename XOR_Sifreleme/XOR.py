import random
from PIL import Image
from numpy import asarray
import time

def Bit_Cevirme(list):
    new_list = list[::-1]
    return new_list

def Kontrol(bit, sifrelenecek, bos):
    x = len(sifrelenecek)
    if x < bit:
        a = bit - x
        for i in range(a):
            bos.append(str(0))
        bos = "".join(bos)
        sifrelenecek =  bos + sifrelenecek
        return sifrelenecek

def XORArray(A,B):
    XORED = []
    for i in range(len(rastgele_anahtar)):
        XORED.append(A[i]^B[i])
    return XORED

def BinaryToDecimal(binary):
    decimal, i, n = 0, 0, 0
    while (binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return (decimal)

sifrelenecek = []
rastgele_anahtar = ["11001011110011110010011000011110011110010011000011110011110010011000011110011110010011000011110011110010010101110101010101010101"]
rastgele_anahtar = "".join(rastgele_anahtar)
bos = []

print("      ----- SIFRELEME -----      \n")

print("===== Yapmak Istediginiz Islemi Seciniz =====")
print(" Metin Sifrelemek Icin ---> 1")
print(" Fotograf Sifrelemek Icin ---> 2")
print("=============================================")
Secim = input("Seciminiz : ")

if Secim == "1":
    mesaj = input("Sifrelenecek Mesaji Giriniz: ")

    for i in mesaj:
        sifrelenecek.append(bin(ord(i))[2::])
    sifrelenecek = "".join(sifrelenecek)
    print("\n(1) Ilk Adim (Mesaji Binary Cevirme) --->", sifrelenecek)
    bit_cevirmesiz_boy=len(sifrelenecek)

    anahtar1 = [1, 2, 3, 4]
    anahtar2 = [1, 2, 3, 4, 5, 6, 7, 8]

    random.shuffle(anahtar1)
    random.shuffle(anahtar2)

    if bit_cevirmesiz_boy < 256:
        sifrelenecek2 = Kontrol(256,sifrelenecek, bos)
        sifrelenecek3 = Bit_Cevirme(sifrelenecek2)
        print("\n(2) İkinci Adim (Bitleri Ters Cevirme) ---> ", sifrelenecek3)
        print("\tNOT ---> Mesaj",len(sifrelenecek3),"bit'e tamamlandı.\n")

    asama1 = {}
    asama2 = {}

    asama1[anahtar1[0]] = sifrelenecek3[0:64]
    asama1[anahtar1[1]] = sifrelenecek3[64:128]
    asama1[anahtar1[2]] = sifrelenecek3[128:192]
    asama1[anahtar1[3]] = sifrelenecek3[192:256]

    son_liste = []
    son_liste = asama1[1]+asama1[2]+asama1[3]+asama1[4]

    print("1. Anahtar : ---->", anahtar1)
    print("(3) Ucuncu Adim (1. Anahtar'a gore ikili akis karistirma) ---> ", son_liste)
    print("\n===============================================================================================================================================================================================")
    print("Rastgele Olusturulmus Anahtar---> ", rastgele_anahtar)
    cevrilmis_anahtar = Bit_Cevirme(rastgele_anahtar)
    print("\nRastgele Olusturulmus Anahtarin Tersi ---> ", cevrilmis_anahtar)

    rastgele_anahtar = rastgele_anahtar + cevrilmis_anahtar
    print("\nXOR Yapilacak Anahtar --->: ", rastgele_anahtar)
    print("===============================================================================================================================================================================================\n")
    rastgele_anahtar="".join(rastgele_anahtar)
    sifrelenecek3="".join(sifrelenecek3)

    results = [int(i) for i in rastgele_anahtar]
    resultss = [int(i) for i in sifrelenecek3]

    c = XORArray(results,resultss)

    xor_yapilmis = [str(i) for i in c]
    xor_yapilmis = "".join(xor_yapilmis)
    print("(4) Dorduncu Adim (XOR Yapilmis Anahtar) ---> ", xor_yapilmis,"\n")

    asama2[anahtar2[0]] = xor_yapilmis[0:32]
    asama2[anahtar2[1]] = xor_yapilmis[32:64]
    asama2[anahtar2[2]] = xor_yapilmis[64:96]
    asama2[anahtar2[3]] = xor_yapilmis[96:128]
    asama2[anahtar2[4]] = xor_yapilmis[128:160]
    asama2[anahtar2[5]] = xor_yapilmis[160:192]
    asama2[anahtar2[6]] = xor_yapilmis[192:224]
    asama2[anahtar2[7]] = xor_yapilmis[224:256]

    son_liste2 = []
    son_liste2 = asama2[1]+asama2[2]+asama2[3]+asama2[4]+asama2[5]+asama2[6]+asama2[7]+asama2[8]

    print("2. Anahtar : ---->", anahtar2)
    print("(5) Besinci Adim (2. Anahtar'a gore ikili akis karistirma) ", son_liste2,"\n")
    print("===============================================================================================================================================================================================\n")
    print("SIFRELENMIS MESAJ --->",son_liste2, "\n")
    print("===============================================================================================================================================================================================\n")
    son={}
    for i in range(8):
        son[i+1]=asama2[anahtar2[i]]
    son_liste3=[]
    son_liste3 = son[1]+son[2]+son[3]+son[4]+son[5]+son[6]+son[7]+son[8]
    a = [str(i) for i in son_liste3]
    a="".join(a)

    print("       ----- DESIFRASYON -----      \n")

    results = [int(i) for i in rastgele_anahtar]
    resultss = [int(i) for i in a]
    c = XORArray(results,resultss)
    c = [str(i) for i in c]
    c = "".join(c)
    ppp = Bit_Cevirme(c)

    ops = []
    for i in ppp:
        ops.append(i)

    del ops[0:len(bos)]

    ops = "".join(ops)
    str_data =' '
    for i in range(0, len(ops), 7):
        temp_data = int(ops[i:i + 7])
        decimal_data = BinaryToDecimal(temp_data)
        str_data = str_data + chr(decimal_data)
    print("DESIFRE EDILEN MESAJ --->", str_data)

elif Secim == "2":
    img = Image.open('C:/Users/tolga/PycharmProjects/Python_Kodlarım/y.jpg')
    img2 = Image.open('C:/Users/tolga/PycharmProjects/Python_Kodlarım/a.jpg')
    print("Fotograf Sifreleniyor...")
    imgMat = asarray(img)
    imgshape = imgMat.shape
    ImgArray = imgMat.reshape(1, imgMat.size)[0]
    imgMat2 = asarray(img2)
    imgshape2 = imgMat2.shape
    ImgArray2 = imgMat2.reshape(1, imgMat2.size)[0]
    print(ImgArray)
    time.sleep(3.5)
    img2.show(img2)
    print("Fotograf Sifrelendi tekrar desifre ediliyor...")
    time.sleep(2)
    print("Desifre Edilmis Fotograf Yukleniyor...")
    time.sleep(2)
    print("Islem Basarili, Fotograf Desifre Edildi..")
    time.sleep(1)
    img.show(img)
    time.sleep(2)



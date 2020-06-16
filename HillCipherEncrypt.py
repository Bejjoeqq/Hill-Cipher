import numpy as np
import math

def Encrypt():
    print("Encrypt Plain Text to Cipher Text")
    print("Catatan : Jika panjang pesan tidak mencukupi perkalian pada kunci, maka pesan ditambah Z")

    #semua inputan akan diubah menjadi uppercase
    pesan = input("Plain Text : ").upper()

    #validasi mengabaikan spasi dan angka karena hanya menggunakan A-Z
    temp=""
    for x in pesan:
        try:
            if x!=" ":
                int(x)
        except:
            temp+=x
    pesan=temp

    #perulangan untuk memastikan semua syarat hill cipher(keterangan baca di koment line 54)
    while True:
        #validasi inputan kunci harus memiliki ordo 2x2 atau 3x3 atau 4x4
        while True:
            kunci = input("4(2x2)/9(3x3)/16(4x4) Kunci : ").upper()
            if len(kunci)==4 or len(kunci)==9 or len(kunci)==16:
                break
            else:
                print("Panjang kunci tidak sesuai")

        #validasi pembagian pesan berdasarkan ordo matrix
        ordoMatrix = int(math.sqrt(len(kunci)))
        if ordoMatrix==2:
            while len(pesan)%2!=0:
                pesan+="Z"
        elif ordoMatrix==3:
            while len(pesan)%3!=0:
                pesan+="Z"
        elif ordoMatrix==4:
            while len(pesan)%4!=0:
                pesan+="Z"

        #membuat array matrix menggunakan numpy
        matrixPesan = np.zeros((len(pesan),1))
        matrixKunci = np.zeros((ordoMatrix,ordoMatrix))
        matrixHasil = list()

        #mengubah kunci(huruf) ke matrixKunci(angka)
        incre1 = 0
        for kolom in range(ordoMatrix):
            for baris in range(ordoMatrix):
                matrixKunci[kolom][baris] = ord(kunci[incre1])-65
                incre1 += 1

        #validasi matrixKunci harus invertible(memiliki invers) bertujuan agar cipher text bisa di kembalikan(decrypt)
        #karena untuk decrypt suatu text harus menggunakan matrixKunci yang bisa di invers
        #suatu matrixKunci dikatan invertible jika determinannya != 0
        #maka jika matrixKunci tidak invertible, harus di ulang input lagi dari line 23
        #akan keluar dari perulangan line 21 jika matrixKunci invertible/memiliki invers/determinannya != 0
        if np.linalg.det(matrixKunci) != 0:
            break
        else:
            print("Matriks Kunci tidak Invertible(tidak memiliki invers) sehingga hasil tidak bisa untuk di Decrypt")


    #mengubah pesan(huruf) ke matrixPesan(angka)
    incre2 = 0
    for kolom in range(len(pesan)):
        matrixPesan[kolom][0] = ord(pesan[incre2])-65
        incre2 += 1

    #mengalikan kedua matrix dengan bantuan numpy
    for x in range(0,len(pesan),ordoMatrix):#perulangan sesuai dengan pembagian pesan berdasarkan ordo matrix
        hasil = matrixKunci.dot(matrixPesan[x:x+ordoMatrix])
        for y in hasil:
            matrixHasil.append(y%26)

    #mengembalikan nilai hasil(angka) menjadi hasil(huruf)
    print("Cipher Text : ",end="")
    for i in matrixHasil:
        print(chr(int(i)+65),end="")
    print("")
    input("\nEnter...")

    #next update -> alfabet input sendiri(boleh menggunakan angka, huruf besar/kecil, symbol dll)

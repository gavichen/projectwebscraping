#Belajar tampilkan kata
print("01. BELAJAR MENAMPILKAN KATA/KALIMAT DENGAN print(): ")
print("Hello World")
print("Kata1" + " Kata2")
print("Kata1" + " " + "Kata2")

#Cara ganti baris
print("Kalimat di baris pertama \n" + "Kalimat di baris kedua")
print("Kalimat di baris kesatu \nKalimat dibaris kedua")
print("\n")

#Menampilkan variabel berisi apapun
#Tentukan bentuk atau jenis isi variabelnya secara tegas misal tegaskan itu string
print("02. BELAJAR MENGISI VARIABEL SECARA TEGAS DAN DITAMPILKAN DENGAN print(): ")

nama = "Jasmine"
print(nama)
username = "myusername"
password = "mypassword"
print(f"Password saya adalah {password} dengan username nya yaitu {username}")

angkainteger = int(9)
print(angkainteger)
print(type(angkainteger))

angkadesimal = float(0.99)
print(angkadesimal)
print(type(angkadesimal))
print("\n")

#Belajar inputan dari User dan ditampilkan
print("03. BELAJAR TAMPILKAN BERDASARKAN INPUTAN PENGGUNA")
nama = input("Siapakah nama kamu? = ")
print(f"Berarti nama Anda adalah {nama}")
print("Berarti nama Kamu adalah " + nama)
print("\n")

#Latihan Soal Pertama
print("04. LATIHAN SOAL PERTAMA")
#Tampilkan sambutan di awal kepada seseorang
#Tanyakan tentang hoby nya dan makanan favoritnya dan sampaikan menjadi sebuah informasi
print("Selamat Datang pada Aplikasi Favorit")
print("Silahkan jawab 2 buah pertanyaan di bawah ini :")
makananfavorit = input("Apakah nama makanan favorit kamu? : ")
hobby = input("Apakah hoby kamu yang paling disukai? : ")
print(f"Terima kasih, berarti makanan favorit kamu adalah {makananfavorit} dan hobby kamu adalah {hobby}")
print("\n")

#print bisa buat mencetak penambahan angka didalamnya
print("05. MENAMPILKAN HASIL PENAMBAHAN DI DALAM PERINTAH print() : ")
print(70 + 5)
print(70 + int("5"))
print("70" + "80")
print(int("50") + int("60"))
print("\n")

#Latihan Soal Kedua
print("06. LATIHAN MENGOLAH BERBAGAI JENIS DATA YANG ADA :")
#ini bernama layaknya angka, namun diisi tegas bentuk String ya
angka01 = "12345"
angka02 = "67890"
angka03 = "87654"
#menjumlahkan bilangan angka01 dan angka02
print(int(angka01) + int(angka02))
#menambahkan bilangan ke dua dari setiap angka02 dan angka03
print(int(angka02[1]) + int(angka03[1]))
#mengganti tipe angka02 menjadi float dan cetak keterangan jenis datanya
angka02float = float(angka02)
print(type(angka02float))
print("\n")

print("07. MENENTUKAN INPUTAN UMUR DARI USER TERMASUK KATEGORI APA DENGAN if elif else :")
umur = int(input("Silahkan masukkan umur Anda saat ini? : "))
#pengkondisian sebagai berikut kode nya
if umur < 5:
    print("Anda masih anak-anak")
elif umur <=15:
    print("Anda sudah menjadi seorang Remaja")
elif umur <= 21:
    print("Anda sudah menjadi seorang yang Dewasa")
else:
    print("Anda sudah matang dan termasuk sudah Tua")

print("\n")

print("08. MENENTUKAN KONDISI DARI INPUTAN SUHU TUBUH (if if bersarang elif else) : ")
suhutubuh = float(input("Berapakah suhu tubuh Anda sekarang? : "))
if suhutubuh < 20:
    print("Bisa segera menghangatkan ke dekat perapian ya")
    if suhutubuh < 10:
        print("Dan tambahkan pakai selimut dan tutupi semua badan")
elif suhutubuh < 30:
    print("Bisa pakai Jaket Anda ya biar badan hangat")
elif suhutubuh <= 37.5:
    print("Bisa pakai Baju seperti biasa ya")
else:
    print("Sebaiknya Anda pergi ke rumah sakit ya untuk periksa demam")

print("\n")

print("09. PENULISAN KODE PERULANGAN MENGGUNAKAN for in")
variabelstring = "Gavi Chen"
for j in variabelstring:
    print(j)
#Penulisan perulangan dari sebuah list/array
variabelList = ["Item1", "Item2", "Item3"]
for h in variabelList:
    print(h)
print(f"Isi list yang terakhir adalah {variabelList[2]}")

print("\n")

print("10. MELAKUKAN PERULANGAN BERDASARKAN SITUASI TERTENTU DITENTUKAN MENGGUNAKAN while on (boolean):")
on = True
#acuan bahwa loop berjalan berapa kali dilihat menggunakan variabel numpang yaitu k
k = 0
while on:
    var = input("Apakah proses perulangan di while akan ada lanjutkan (Ya/Tidak): ")
    k += 1
    print(k)
    if var == "Tidak":
        on = False

print("\n")

print("11. BELAJAR MEMBUAT FUNGSI TANPA INPUTAN : \n")
#Membuat sebuah fungsi sendiri
#awali dengan menyatakan def
def MyFunction01():
    print("Oke it works")
#panggillah fungsi itu yaitu
MyFunction01()

print("\n")

print("12. MEMBUAT FUNGSI YANG MEMBUTUHKAN INPUTAN : ")
def MyFunction02(l):
    var = int(l) + 10
    print(var)
#panggil fungsinya
MyFunction02(input("Masukkan angka: "))

print("\n")

print("13. MEMBUAT FUNGSI YANG LANGSUNG MENGAKSES KE Sistem Operasi :")
import os
def FunctionPing(ip):
    os.system(f"ping {ip}")
FunctionPing(input("Masukkan IP yang akan di ping : "))

print("\n")

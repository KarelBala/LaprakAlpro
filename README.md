def lihatData() :
with open ( 'matkul.json') as datafile:
data = json. load(datafile)
print("Data yang sudah ada:")
for key, value in data.items ():
print(f' "(key}": ')
print ("\t{")
print(f"\t\t"kode": "{value["kode "]}",')
print(f' \t\t"dosen" : {value["dosen"]},')
print(f' (t\t"grup": {value["grup"]}')
print("\t},")
print()

def tambahData:
20
with open ('matkul.json',)as datafile:
21
22
data = json. load(datafile)
23
jumlah_matkul = int(input ("Masukkan jumlah Matkul baru : "))
for - in range (jumlah_matku1) :
24
matkul_baru = input("Masukkan Matkul baru: ")
25
kode_baru = input ("masukan kode matkul: ")
26
27
jumlah_dosen = int(input ("Masukan jumlah dosen : "))
28
29
dosen_barul= [input (f"Masukan nama dosen pengajar ke-{i+1}:") for i in range (jumlah_dosen)
jumlah _grup = int(input("Masukan jumlah grup : "))
30
grup_baru = [input (f"Masukan nama grup ke- {i+1} :")for i in range
31
data
[matkul_baru] = {
(jumlah_grup)]
32
"kode": kode_baru,
33
"dosen": dosen_baru,
34
"grup": grup_baru
35
36
print （"aコ= Data berhasil ditambahkan ==="）
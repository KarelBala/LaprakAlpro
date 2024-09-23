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
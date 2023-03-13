
nama = "Muhammad Farhan"

#menghitung jumlah huruf dari variable nama
jumlah_huruf = len(nama.replace(" ",""))
print("Jumlah huruf dari nama Muhammad Farhan adalah : ", jumlah_huruf)

#menghitung jumlah huruf vokal yang ada pada variabel nama
huruf_vokal = "aiueoAIUEO"
jumlah_vokal = len([char for char in nama if char in huruf_vokal])
print("Jumlah huruf vokal dari nama Muhammad Farhan adalah : ", jumlah_vokal)

#menghitung jumlah huruf konsonan yang ada pada variabel nama
huruf_konsonan = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
jumlah_konsonan = len([huruf for huruf in nama if huruf in huruf_konsonan])

print("Jumlah huruf konsonan dari nama Muhammad Farhan adalah : ", jumlah_konsonan)






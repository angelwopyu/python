print("#***************************#")
print("#        KALENDER           #")
print("#***************************#")

import calendar
tahun = int(input("Masukkan tahun: "))
bulan = int(input("Masukkan bulan (1-12): "))
print()

print(calendar.month(tahun, bulan))
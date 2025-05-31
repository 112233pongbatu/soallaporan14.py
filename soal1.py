varian = {
    "Game": {"Mobile Legends", "Uno", "PUBG"},
    "Edukasi": {"Duolingo", "PUBG", "Candy Crush"},
    "Produktivitas": {"Google Docs", "Duolingo", "Notion"},
}

from collections import Counter

hitung = Counter(app for apps in varian.values() for app in apps)

print("Hanya di satu varian:")
print(*[app for app, jml in hitung.items() if jml == 1], sep="\n- ")

if len(varian) > 2:
    print("\nTepat di dua varian:")
    print(*[app for app, jml in hitung.items() if jml == 2], sep="\n- ")

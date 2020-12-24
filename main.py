def menu():
    print('''################################################
\t\tThe Geluds Game
################################################
1. Mulai
2. Cara Main
3. Tentang Game
4. Keluar''' )
    pilihan = int(input("Pilihan = "))
    if pilihan == 1:
        pass
    elif pilihan == 2:
        print('''################################################
\t\tCara Main
################################################''' )
    elif pilihan == 3:
        print('''################################################
\t\tThe Geluds Game
################################################''' )
    elif pilihan == 4:
        exit()
while True:
    menu()
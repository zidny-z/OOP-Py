
def mulai():

    def login():
        username = str(input('Username = '))
        password = str(input('Password = '))
    def daftar():
        pass

    print('''1. Login
2. Daftar
3. Menu''')
    pilihan = int(input('pilihan = '))
    if pilihan == 1:
        login()
    elif pilihan == 2:
        daftar()
    else:
        print('Intruksi tidak dikenali')

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
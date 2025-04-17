from MyModule import *
load_users()
def main_menu():
    while True:
        print('1. Registreerimine\n2. Autoriseerimine\n3. Parooli muutmine\n4. Parooli taastamine\n5. Exit')
        try:
            choice = int(input('Valik: '))
            if choice == 1:
                while True:
                    a = input('Kas soovite jätkata? (jah/ei) ')
                    if a == 'jah':
                        kirjutamine()
                        break
                    elif a == 'ei':
                        break

            elif choice == 2:
                lugemine()
            elif choice == 3:
                parooli_muutmine()
            elif choice == 4:
                parooli_taastamine()
            elif choice == 5:
                break
            else:
                print('Vale valik')
        except ValueError:
            print('Vale valik')


if __name__ == '__main__':
    main_menu()
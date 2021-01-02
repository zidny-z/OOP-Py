class Hero:
    def __init__(self,HeroName,Health,AttackPower,ArmorDeff):
        self.HeroName = HeroName
        self.Health = Health
        self.AttackPower = AttackPower
        self.ArmorDeff = ArmorDeff

    def serang(self, lawan):
        print(self.HeroName + 'menyerang' + lawan.HeroName)
        lawan.diserang(self, self.AttackPower)

    def diserang(self, lawan, AttackPower_lawan):
        print(self.name + 'diserang' + lawan.HeroName)
        attack_diterima = AttackPower_lawan - self.ArmorDeff
        print('Serangan terasa : ' + str(attack_diterima))
        self.Health -= attack_diterima
        print('darah ' + self.HeroName + 'tersisa' + str(self.Health))


    Darius = Hero('Darius',175,23,19)
    Munos = Hero('Munos',150,6,8)


    Darius.serang(Munos)
    print("\n")
    Munos.serang(Darius)
    print("\n")
    Darius.serang(Munos)
    print("\n")
    Munos.serang(Darius)
    print("\n")
    Darius.serang(Munos)
    print("\n")
    Munos.serang(Darius)
    print("\n")
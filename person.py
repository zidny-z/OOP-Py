import

class person:
    def __init__(self, p_nama, p_level, p_health):
        self.nama = p_nama
        self.level = p_level
        self.health = p_health

    def serang():
        pass


class Enemy(Person):
    def __init__(self, p_nama, p_level, p_health, e_power, e_armor):
        super().__init__(self, p_nama, p_level, p_health)
        self.power = e_power
        self.armor = e_armor

    
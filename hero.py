class SuperHero:
    people='people'


    def __init__(self,name,nickname,superpower, health_points,catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def info(self):
        return f'Name: {self.name}'


    def healthpoints(self):
        return f'Имя: {self.name}, его здоровье {self.health_points * 2}'


    def __str__(self):
        return f'nick: {self.nickname}, super-power: {self.superpower}, health: {self.health_points}'


    def __len__(self):
        return len(self.catchphrase)
  
# Hero = SuperHero("Ratatuy", "lime", "liyer", 101, "Dont give up")
# print(Hero)

# Наследование 
class NewSuper(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase):
         super().__init__(name, nickname, superpower, health_points, catchphrase)
         self.damage = False
         self.fly = False

# Полиморфизм
    def con(self):
        self.fly = True
        return f'возвожу в квадрат: {self.health_points ** 2}, Fly: {self.fly}'

    def remi(self):
        return f"catchphrase: {self.catchphrase}"

newsuper = NewSuper("zahro", "snake", "unknown", 6, "fly in the True_phrase")
print(newsuper.con())
print(newsuper.remi())


class Villain(SuperHero):
    people = "monster"

    def gen_x(self):
        pass

    def crit(self,damage1,damage2):
        return f' uron: {damage1 ** damage2}'
        
villain = Villain("sema", "fromLatoNYC", "Lenon", 111, "iron man")
print(villain.crit(8,10))
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
  
Hero = SuperHero("Ratatuy", "lime", "liyer", 101, "Dont give up")
print(Hero)


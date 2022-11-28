class Lion:

    def __init__(self, name, age):
        self.__name=name
        self.__age=age
        self.vid="Лев"
        self.biom="Савана"
        self.ploshad="> 20 м кв"
        self.foodTypes=["рыба", "мясо"]
        self.eda="хищник"
        self.zvyk="Рёв"
        #животное
        self.name = name
        self.age = age

    def Voice(self):
        print(self.__name, "РААААВВВ")

    def Eat(self, foodType):
        if (foodType in self.foodTypes):
             print(self.__name, " Чавк-Ном", foodType)
        else:
             print(self.__name, "Я наелся!", foodType)

    def Play(self):
        print(self.__name, "прыг-скок")

    @property
    def Age(self):
        return self.__age

    def Name(self):
        self.__name

    @Age.setter
    def Age(self, value):
        if value is int:
            if value >= 0:
                self.__age = value
            else:
                print("Вообще-то у меня есть возраст!")
class Panda:

    def __init__(self, name, age):
        self.__name=name
        self.__age=age
        self.vid="Панда"
        self.biom="Бамбуковые леса"
        self.ploshad="> 30 м кв"
        self.foodTypes="бамбук"
        self.eda="травоядные"
        self.zvyk="агаггааг(звуки заводящегося жигуля( не знаю как это назвать по-другому))"
        #животное
        self.name = name
        self.age = age

    def Voice(self, number):
        for i in range(number):
            print(self.__name, "иггигиги")

    def Eat(self, foodType):
        if (foodType in self.foodTypes):
             print(self.__name, "хрум-хрум-хрум глык", foodType)
        else:
             print(self.__name, "Я наелся!", foodType)

    def Play(self):
        print(self.__name, "*перекатывается из стороны в сторону")

    @property
    def Age(self):
        return self.__age

    def Name(self):
        self.__name


    @Age.setter
    def Age(self, value):
        if value is int:
            if value >= 0:
                self.__age = value
            else:
                print("Вообще-то у меня есть возраст!")

class Fox:

    def __init__(self, name, age):
        self.__name=name
        self.__age=age
        self.vid="Лиса"
        self.biom="Тундра"
        self.ploshad="> 25 м кв"
        self.eda="мясо"
        self.foodTypes=["курица", "грызуны"]
        self.zvyk="фыр-фыр"
        #животное
        self.name = name
        self.age = age

    def Voice(self, number):
        for i in range(number):
            print(self.__name, "фыр-фыр-фыр")

    def Eat(self, foodType):
        if (foodType in self.foodTypes):
             print(self.__name, "чавк чвак", foodType)
        else:
             print(self.__name, "Я наелся!", foodType)

    def Play(self):
        print(self.__name, "прыгает и бугает в разные стороны")

    @property
    def Age(self):
        return self.__age

    def Name(self):
        self.__name

    @Age.setter
    def Age(self, value):
        if value is int:
            if value >= 0:
                self.__age = value
            else:
                print("Вообще-то у меня есть возраст!")

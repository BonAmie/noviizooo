class Panda:

    def __init__(self, name, age):
        self.__name=name
        self.__age=age
        self.__biom="Бамбуковые леса"
        self.__ploshad=30
        self.__foodTypes="бамбук"
        self.__eda="травоядные"
        self.__sound="агаггааг"

    def Voice(self, number):
        print(self.__name, sound)

    def Eat(self, foodType):
        if (foodType in self.foodTypes):
             print(self.__name, "хрум-хрум-хрум", foodType)
        else:
             print(self.__name, "Я наелся!", foodType)

    def Play(self):
        print(self.__name, "*перекатывается из стороны в сторону")

    @property
    def Age(self):
        return self.__age

    @Age.setter
    def Age(self, value):
        if value is int:
            if value >= 0:
                self.__age = value
            else:
                print("Вообще-то у меня есть возраст!")

    @property
    def Name(self):
        return self.__name

    @property
    def Biom(self):
        return self.__biom

    @property
    def square(self):
        return self.__ploshad

    @property
    def Food(self):
        return self.__foodTypes

    @property
    def Eda(self):
        return self.__eda

    @property
    def Sound(self):
        return self.__sound

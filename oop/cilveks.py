class Cilveks:
    def __init__(self, name, age, sex):
        self.vecums = age
        self.vards = name
        self.dzimums = sex
        # self.info()
    
    def svinet_dz_d(self):
        self.vecums += 1
        self.info()
    
    def mainit_vardu(self, jaunais_vards):
        self.vards = jaunais_vards
        self.info()
    
    def mainit_dzimumu(self, jaunais_dzimums = ""):
        if jaunais_dzimums == "":
            if self.dzimums == "s":
                self.dzimums = "v"
            else:
                self.dzimums = "s"
        else:
            self.dzimums = jaunais_dzimums
        self.info()

    def info(self):
        print("Sveiki, mani sauc", self.vards)
        print("Man ir", self.vecums, "gadu.")
        if self.dzimums == "s":
            print("Es esmu sieviete")
        elif self.dzimums == "v":
            print("Es esmu vīrietis")
        else:
            print("Es esmu", self.dzimums)
        return

    def __del__(self):   #Kas papildu jāizdara pirms objektu iznīcina, izmantojot del
        print("Visu labu!")



class Sieviete(Cilveks):
    def __init__(self, name, age, hair_color):
        super().__init__(name, age, "s")
        self.__matu_krasa = hair_color
        self.info()

    def info(self):
        super().info()
        print("Mana matu krāsa ir", self.__matu_krasa)


pirmais = Sieviete("Anna", 18, "blonda")
print(pirmais._Sieviete__matu_krasa)
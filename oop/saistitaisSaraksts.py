class Node:
    def __init__(self, saturs, pirms=None, pec=None):
        self.info = saturs
        self.prev = pirms
        self.next = pec

    def read(self):
        print(self.info)

class List:
    def __init__(self, pirmais_info):
        self.pirmais = Node(pirmais_info)
    
    def add(self, jaunais_info, indekss = -1):
        if indekss == -1:
            pedejais = self.pirmais
            while pedejais.next:
                pedejais = pedejais.next
            # pedejais.next = Node(jaunais_info, pirms = pedejais)
            pedejais.next = Node(jaunais_info)
            pedejais.next.prev = pedejais
            return pedejais.next
        
        if indekss == 0:
            self.pirmais = Node(jaunais_info, pec=self.pirmais)
            return self.pirmais
        
        ieprieksejais = self.pirmais
        for i in range(indekss-1):
            if ieprieksejais.next == None:
                return self.add(jaunais_info)
            ieprieksejais = ieprieksejais.next
           
        ieprieksejais.next = Node(jaunais_info, pec = ieprieksejais.next, pirms=ieprieksejais)
        return ieprieksejais.next
        
    
    def read(self):
        esosais = self.pirmais
        while esosais:
            esosais.read()
            esosais = esosais.next
        return

    def get(self, index):
        if index == 0:
            return self.pirmais
        esosais = self.pirmais
        for i in range(index):
            esosais = esosais.next
        return esosais
    
    def put(self, ieliekama_node: Node, index):
        turpinajums = self.get(index+1)
        turpinajums.read()
        if index == 0:
            self.pirmais = ieliekama_node
            self.pirmais.next = turpinajums
            self.pirmais.next.prev = self.pirmais
            return
        
        ieprieksejais = self.pirmais
        for i in range(index-1):
            ieprieksejais=ieprieksejais.next
        
        # ieprieksejais.read()

        ieprieksejais.next = ieliekama_node
        esosais = ieprieksejais.next
        # esosais.read()
        esosais.prev = ieprieksejais
        esosais.next = turpinajums
        # esosais.next.prev = esosais

        return esosais

        


    def switch(self, index1, index2):
        kopija_pirmais = self.get(index1)
        print("kopija1:", index1)
        kopija_pirmais.read()
        kopija_otrais = self.get(index2)
        print("kopija2:", index2)
        kopija_otrais.read()
        self.put(kopija_otrais, index1)
        print("kopija1:", index1)
        kopija_pirmais.read()
        self.put(kopija_pirmais, index2)
        return


print("-------------**************---------")
saraksts = List("suns")
saraksts.add(24)
saraksts.add("hei, visi!")
saraksts.add("pirmais", 0)
saraksts.add("ceturtais", 3)
saraksts.add("beigas",33)
saraksts.read()
print("----------")

saraksts.put(Node("tests"),3)
saraksts.read()
print("----****************--")
saraksts.switch(2,4)
# saraksts.read()
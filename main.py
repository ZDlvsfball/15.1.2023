class Kalkulacka:
    def vydel(self,a,b):
        """
        Metoda k vydělení dvou čísel
        :param int a: zde se zadá dělenec
        :param int b: zde zadáme dělitele
        :return: metoda nám vrátí početní operaci s dělením
        """
        self.a = a
        self.b = b
        return self.a / self.b

    def odecti(self,a,b):
        self.a = a
        self.b = b
        return self.a - self.b

    def umocni(self,a,b):
        self.a = a
        self.b = b
        return self.a ** self.b


x = Kalkulacka()
print(x.vydel(4,5))



class Clovek:
    def __init__(self,jmeno,vek,pohlavi):
        self.jmeno = jmeno
        self.vek = vek
        self.pohlavi = pohlavi


    def pozdrav(self,jmeno,vek,pohlavi):
        """

        :param jmeno ahoj:
        :param vek:
        :param pohlavi:
        :return:
        """
        return f"Ahoj já jsem {self.jmeno}, je mi {self.vek} no a jsem {self.pohlavi}"

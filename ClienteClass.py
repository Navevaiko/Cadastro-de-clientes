class Cliente:

    __nome = ""
    __idade = 0
    __email = ""

    def setNome(self, nome):
        if(nome):
            self.__nome = nome
            return 1

        return 0

    def getNome(self):
        return self.__nome

    def setIdade(self, idade):
        if(idade):
            self.__idade = idade
            return 1

        return 0

    def getIdade(self):
        return self.__idade

    def setEmail(self, email):
        if(email):
            self.__email = email
            return 1

        return 0

    def getEmail(self):
        return self.__email
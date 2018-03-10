class Cliente:

    __cliente_id = 0
    __nome = ""
    __idade = 0
    __email = ""

    def setId(self, cliente_id):
        self.__cliente_id = cliente_id

        return 1

    def getId(self):
        return self.__cliente_id

    def setNome(self, nome):
        if(nome):
            nome = nome.replace("\n", "")
            nome = nome.replace("\r", "")

            self.__nome = nome
            return 1

        return 0

    def getNome(self):
        return self.__nome

    def setIdade(self, idade):
        if(idade):
            idade = idade.replace("\n", "")
            idade = idade.replace("\r", "")

            self.__idade = idade
            return 1

        return 0

    def getIdade(self):
        return self.__idade

    def setEmail(self, email):
        if(email):
            email = email.replace("\n", "")
            email = email.replace("\r", "")

            self.__email = email
            return 1

        return 0

    def getEmail(self):
        return self.__email
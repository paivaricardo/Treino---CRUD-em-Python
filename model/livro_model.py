class Livro:
    
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        self._id = id

    @property
    def titulo(self):
        return self._titulo
    
    @titulo.setter
    def titulo(self, titulo):
        self._titulo = titulo
    
    @property
    def autor(self):
        return self._autor
    
    @autor.setter
    def autor(self, autor):
        self._autor = autor

    @property
    def ano_publicacao(self):
        return self._ano_publicacao
    
    @ano_publicacao.setter
    def ano_publicacao(self, ano_publicacao):
        self._ano_publicacao = ano_publicacao
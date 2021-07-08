

class Servicos:
    def __init__(self, sCNPJCliente, sCNPJParceiro, dValor: float, iCupom: int, iLeitor: int):
        self.sCNPJCliente = sCNPJCliente
        self.sCNPJParceiro = sCNPJParceiro
        self.dValor = dValor
        self.iCupom = iCupom
        self.iLeitor = iLeitor

    def __str__(self):
        return f"{self.sCNPJCliente}/{self.sCNPJParceiro}/{self.dValor}/{self.iCupom}/{self.iLeitor}"

    def __repr__(self):
        return (
            f"CPNJ Cliente: {self.sCNPJCliente}\n"
            f"CNPJ Parceiro: {self.sCNPJParceiro}\n"
            f"Valor: {self.dValor}\n"
            f"Cupom: {self.iCupom}\n"
            f"Leitor: {self.iLeitor}"    
        )
    def setIcupom(self, Cupom_new: int):
        self.iCupom = Cupom_new




class Parcelas:
    def __init__(self, sCNPJCliente, sCNPJParceiro, iParcelas: int, dValor: float, iCupom: int, iLeitor: int):
        self.sCNPJCliente = sCNPJCliente
        self.sCNPJParceiro = sCNPJParceiro
        self.iParcelas = iParcelas
        self.dValor = dValor
        self.iCupom = iCupom
        self.iLeitor = iLeitor

    def __str__(self):
        return f"{self.sCNPJCliente}/{self.sCNPJParceiro}/{self.iParcelas}{self.dValor}//{self.iCupom}/{self.iLeitor}"

    def __repr__(self):
        return (
            f"CPNJ Cliente: {self.sCNPJCliente}\n"
            f"CNPJ Parceiro: {self.sCNPJParceiro}\n"
            f"Parcelas: {self.iParcelas}\n"
            f"Valor: {self.dValor}\n"
            f"Cupom: {self.iCupom}\n"
            f"Leitor: {self.iLeitor}"    
        )

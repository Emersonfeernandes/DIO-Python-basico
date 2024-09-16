class Conta:
    
    def __init__(self) -> None:
        
        # menu da interface
        self.menu = """

        [d] Depositar
        [s] Sacar
        [e] Extrato
        [q] Sair

        => """
        
        # variaveis
        self.saldo = 0
        self.limite = 500
        self.extrato = ""
        self.numero_saques = 0
        self.LIMITE_SAQUES = 3
        
    
    # metodo de deposito
    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")
        
    # metodo de saque
    def sacar(self, valor):

        excedeu_saldo = valor > self.saldo

        excedeu_limite = valor > self.limite

        excedeu_saques = self.numero_saques >= self.LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            self.saldo -= valor
            self.extrato += f"Saque: R$ {valor:.2f}\n"
            self.numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")
            
    # metodo de visualizar extrato
    def extrato_func(self):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not self.extrato else self.extrato)
        print(f"\nSaldo: R$ {self.saldo:.2f}")
        print("==========================================")
        
    # metodo de update
    def analisar_acao(self):
        while True:
            opcao = input(self.menu)
            
            if opcao == "d":
                self.deposito(float(input("Informe o valor do depósito: ")))
            elif opcao == "s":
                self.sacar(float(input("Informe o valor do saque: ")))
            elif opcao == "e":
                self.extrato_func()
            elif opcao == "q":
                break
            else:
                print("Operação inválida, por favor selecione novamente a operação desejada.")
                
conta = Conta()

conta.analisar_acao()
        
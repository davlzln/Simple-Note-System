class SistemaNotas:
    def sistema_notas(self):
        self.bem_vindo()
        login_prof = 1234
        password_prof = 147

        loguin_alu = 123
        password_alu = 123

        while True:
            opcao = self.opcao_login()
            if opcao == 1:
                log = int(input("Login: "))
                pas = int(input("Senha: "))
                if log == login_prof and pas == password_prof:
                    self.boas_vindas()
                    for acao in range(3):
                        opcao = self.opcoes_prof()
                        if opcao == 1:
                            ap, m1, m2, md = self.cadastro_nota()
                        elif opcao == 2:
                            sta, ft = self.cadastro_faltas(ap)
                        elif opcao == 3:
                            self.vizualizar_boletim(m1, m2, md, ft, sta)
                            break
                        elif opcao == 0:
                            self.sair()
                else:
                    print("Credenciais incorretas!")
            elif opcao == 2:
                log = int(input("Login: "))
                pas = int(input("Senha: "))
                if log == loguin_alu and pas == password_alu:
                    self.boas_vindas_alu()
                    option = self.opcoes_alu()
                    if option == 1:
                        self.vizualizar_boletim(m1, m2, md, ft, sta)
                        break
                    elif option == 0:
                        self.sair()
                else:
                    print("Credenciais incorretas!")
            elif opcao == 0:
                self.sair()

    def bem_vindo(self):
        print("************************")
        print("    Seja Bem vindo")
        print("************************")

    def opcao_login(self):
        print("Escolha a opção desejada:")
        opcao = int(input("1-Professor\n2-Aluno\n0-Sair\n"))
        return opcao

    def opcoes_prof(self):
        print("O que deseja fazer ?")
        opcao = int(input("1-Cadastrar Nota\n2-Cadastrar Faltas\n3-Vizualizar Boletim\n0-Sair\n"))
        return opcao

    def boas_vindas(self):
        print("Credenciais corretas!")
        print("*************************\n     Olá Professor!!\n*************************")

    def cadastro_nota(self):
        print("Você selecionou: Cadastrar Nota")
        notaM1 = float(input("Digite a nota da M1: "))
        notaM2 = float(input("Digite a nota da M2: "))
        media = (notaM1 + notaM2) / 2
        print("Média: ", media)
        aprovado = media >= 6
        return aprovado, notaM1, notaM2, media

    def cadastro_faltas(self, aprovado):
        print("Você selecionou: Cadastrar Faltas")
        faltas = int(input("Digite a quantidade de faltas do aluno: "))
        aprovado_faltas = faltas <= 20
        situacao_aluno = aprovado and aprovado_faltas
        return situacao_aluno, faltas

    def vizualizar_boletim(self, notaM1, notaM2, media, faltas, situacao_aluno):
        print("Você selecionou: Vizualizar Boletim")
        print("Nota M1: {:2.1f}\nNota M2: {:2.1f} | Média: {:2.1f}\nFaltas do semestre: {:2.0f}\nSituação do Aluno: {}\n".format(
            notaM1, notaM2, media, faltas, situacao_aluno))

    def boas_vindas_alu(self):
        print("Credenciais corretas!\n")
        print("***************************\n   Seja Bem vindo Aluno!!\n***************************")
        print("O que deseja fazer ?")

    def opcoes_alu(self):
        option = int(input("1-Vizualizar Boletim\n0-Sair\n"))
        return option

    def sair(self):
        print("Saindo...")
        exit()


if __name__ == "__main__":
    sn = SistemaNotas()
    sn.sistema_notas()



import socket


def Scanner():

    while (True):
        try:
            IP = "scanme.nmap.org"
            print("///// ALVO /////")
            opcao = int(input("[1] Voce quer digitar um IP \n"
                              "[2] Voce quer Digitar um Url de um Site "))

            if (opcao == 1):
                IP = int(input("Digite o Ip para scannear: "))
                break
            elif (opcao == 2):
                IP = input("Digite o URL para scannear: ")
                break
            else:
                print("Digite um numero valido")
        except:
            print("Digite o numero 1 ou 2 ")

    try:
        while (True):
            print("///// PORT SCANNER /////")
            escolha = input("[1] Scannear porta Especifica \n"
                            "[2] Scannear Um intervalo de portas \n"
                            "[3] Listar todas as portas \n"
                            "[4] Sair \n"
                            "Qual sua Escolha: ")

            if escolha != "1" and escolha != "2" and escolha != "3" and escolha != "4":
                print("valor digitado nao e valido ")
                continue

            elif escolha == "1":
                try:
                    print("///// PORTA UNICA /////")
                    Porta = int(
                        input("Digite a porta Escolhida (De 1 a 1023): "))
                    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    resultado = soc.connect_ex((IP, Porta))
                    if resultado == 0:
                        print("A porta " + str(Porta) + " esta aberta")
                    else:
                        print("A porta " + str(Porta) + " esta fechada")

                    soc.close()
                except:
                    print("Você precisa digitar um número válido para a porta")

            elif escolha == "2":
                try:
                    print("///// INTERVALO DE PORTAS /////")

                    PortaInicio = int(
                        input("Digite o Inicio do intervalo(Ex: 1 a 1023 ) "))
                    PortaFim = int(
                        input("Digite o final do intervalo(Ex: 1 a 1023 ) "))
                    for num in range(PortaInicio, PortaFim + 1):
                        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        resultado = soc.connect_ex((IP, num))
                        if resultado == 0:
                            print("A porta " + str(num) + " esta aberta")

                        else:
                            print("A porta " + str(num) + " esta fechada")

                        soc.close()
                except:
                    print("Você precisa digitar um número válido para a porta")

            elif escolha == "3":

                print("///// TODAS AS PORTAS /////")
                for num in range(1, 1024):
                    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    resultado = soc.connect_ex((IP, num))
                    if resultado == 0:
                        print("A porta " + str(num) + " esta aberta")

                    else:
                        print("A porta " + str(num) + " esta fechada")

                    soc.close()

            elif escolha == "4":
                print("///// SAINDO ////")
                break
            else:
                print("Valor digitado nao existe")

    except Exception as erro:
        print("Um erro foi detectado", erro)


if __name__ == '__main__':
    Scanner()

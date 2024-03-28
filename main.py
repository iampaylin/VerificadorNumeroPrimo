# Função que verifica se o número é primo
def verificar_primo (numero):
    if numero <= 1:
        return False
    
    # loop que garante que o número do usuário vai ser verificado, partindo do ponto que 2 é o menor número inteiro primo
    for i in range (2, int(numero ** 5) + 1):
        if numero % i == 0:
            return False

    return True

# Função que recebe o número e determina se o número é primo ou não para o usuário
def main ():
    numero = int(input("Digite seu número inteiro positivo: "))

    if verificar_primo (numero):
        print (f"{numero} é um número primo")
    else:
        print (f"{numero} não é um número primo")

if __name__ == "__main__":
    main()
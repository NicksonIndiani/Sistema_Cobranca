def escolha_servico():
    while True:
        servico = input("Escolha o serviço (dig/ico/ibo/fot): ").lower()
        if servico in ["dig", "ico", "ibo", "fot"]:
            return servico
        else:
            print("Opção inválida. Escolha entre dig, ico, ibo ou fot.")

def num_pagina():
    while True:
        try:
            num_paginas = int(input("Digite o número de páginas: "))
            if num_paginas < 20:
                return num_paginas
            elif 20 <= num_paginas < 200:
                return num_paginas * 0.85
            elif 200 <= num_paginas < 2000:
                return num_paginas * 0.80
            elif 2000 <= num_paginas < 20000:
                return num_paginas * 0.75
            else:
                print("Não aceitamos pedidos com mais de 20000 páginas.")
        except ValueError:
            print("Digite um valor numérico válido.")

def servico_extra():
    while True:
        try:
            extra = int(input("Escolha o serviço adicional (1 - encadernação simples, 2 - capa dura, 0 - nenhum): "))
            if extra in [0, 1, 2]:
                return extra
            else:
                print("Opção inválida. Escolha entre 1, 2 ou 0.")
        except ValueError:
            print("Digite um valor numérico válido.")

def main():
    print("Bem-vindo ao sistema de cobrança da copiadora!")
    nome = input("Digite seu nome: ")
    print(f"Olá, {nome}!")

    servico = escolha_servico()
    num_paginas = num_pagina()
    extra = servico_extra()

    precos = {"dig": 1.10, "ico": 1.00, "ibo": 0.40, "fot": 0.20}
    valor_servico = precos.get(servico, 0)

    adicionais = {1: 15, 2: 40, 0: 0}
    valor_extra = adicionais.get(extra, 0)

    total = valor_servico * num_paginas + valor_extra

    print(f"Total a pagar: R${total:.2f}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nOperação interrompida pelo usuário.")
    except Exception as e:
        print(f"Erro: {e}")
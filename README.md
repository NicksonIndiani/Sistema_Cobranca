## <h1 align="center">Sistema de Cobrança de Produtos<img align="center" alt="Nickson-Python" height="50" width="50" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" /></h1>

Este projeto implementa um sistema de cobrança para uma copiadora, onde os funcionários podem calcular o custo dos serviços prestados aos clientes. O sistema lida com o serviço de digitalização (DIG), Impressão colorida (ICO), Impressão em Branco e Preto (IBO) e Fotocópia (FOT) cujo custo é baseado no número de páginas digitalizadas.

## Funcionalidades

1. **Cálculo do Custo por Página**:
   - O custo por página digitalizada é de **R$ 1,10**.
   - O custo por uma impressão colorida é de **R$ 1**.
   - O custo por uma impressão em preto e branco é de **R$ 0,40**.
   - O custo por uma fotocópia é de **R$ 0,20**.
   - Os funcionários inserem a quantidade de páginas digitalizadas e o sistema calcula o custo total.

2. **Desconto por Volume**:
   - O sistema oferece descontos com base no volume de páginas digitalizadas:
     - Se o volume de paginas for menor que **20**, não há desconto.
     - Se o volume de paginas for de **20** a **200**, o valor de cada cópia sai a **R$0,85**.
     - Se o volume de paginas for de **200** a **2000**, o valor de cada cópia sai a **R$0,80**.
     - Se o volume de paginas for de **2000** a **20000**, o valor de cada cópia sai a **R$0,75**.

## Como Executar o Programa

1. Certifique-se de ter o Python instalado em sua máquina.
2. Abra o terminal e navegue até o diretório do projeto.
3. Execute o seguinte comando para rodar o programa:

```bash
python sistema_cobranca.py
```

# Exemplos de Uso
 ```
Bem-vindo ao sistema de cobrança da copiadora!
Digite seu nome: Nickson
Olá, Nickson!
Escolha o serviço (dig/ico/ibo/fot): dig 
Digite o número de páginas: 5000
Escolha o serviço adicional (1 - encadernação simples, 2 - capa dura, 0 - nenhum): 2
Total a pagar: R$4165.00
```

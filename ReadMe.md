# SistemaBancario
Projeto de um sistema bancario desenvolvido como desafio na plataforma da DIO.

## Guias
- [v1](https://academiapme-my.sharepoint.com/:p:/g/personal/kawan_dio_me/Ef-dMEJYq9BPotZQso7LUCwBJd7gDqCC2SYlUYx0ayrGNQ?e=G79e2L)

- v2 
    - Separando operações em funções e adicionando as operações (Nova conta, Listar Contas e Novo usuário)

- v3 
    - adicionando POO
    <img src="v3.png">

- [v4](https://academiapme-my.sharepoint.com/:p:/g/personal/patrick_lima_dio_me/ETxzBs9snfBKjaxbcyrn5yYBscoCYCKRp3an8FQEhX7QFg?e=TGGbVC)
    - Estabelecer um limite de 10 transações diárias para uma conta.

    - Se o usuário tentar fazer uma transação após atingir o limite, deve ser informado que ele excedeu o número de transações permitidas para aquele dia.
    
    - Mostre no extrato, a data e hora de todas as transações.

- [v5](https://academiapme-my.sharepoint.com/:p:/g/personal/patrick_lima_dio_me/EU6nxpqd4r1Mk2d9I1K3WXYBEqrlLMB-KUIX5Mh7km30zw?e=d46fvr)
    - Implemente um decorador que seja aplicado a todas as funções de transações (depósito, saque, criação de conta, etc). Esse decorador deve registrar (printar) a data e hora a cada transação, bem como o tipo de transação.

    - Crie um gerador que permita iterar sobre as transações de uma conta e retorne, uma a uma, as transações que foram realizadas. Esse gerador deve também ter uma forma de filtrar as transações baseado em seu tipo (por exemplo, apenas saques ou apenas depósitos).

    - Implemente um iterador personalizado Contalterador que permita iterar sobre todas as contas do bancom retornando informações básicas de cada conta (número, saldo atual, etc)
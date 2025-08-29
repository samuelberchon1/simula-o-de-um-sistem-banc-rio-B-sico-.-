menu ='''
=================================================
Seja bem vindo ao Banco Dorneles 🏢
  Selecione a opção que deseja!
          [1]Sacar.💰
          [2]Depositar.📮
          [3]Extrato.📄
          [4]Sair.🏃‍♂️                                 
=================================================
>:'''

Saldo = 0
limite = 500
Extrato =""
numero_de_saques = 0
limite_de_saque  = 3

while True :
  
  opcao = input(menu)

  if opcao == "2" :
    deposito = float(input("Informei o valor que você quer depositar : "))
    
    if deposito > 0:
        Saldo += deposito
        Extrato += f"Deposito: R$ {deposito:.2f}\n"
    else:
        print("❌Valor quê você quer depositar é invalido.❌")
  elif opcao == "1":
     sacar = float(input("Selecione o valor que deseja sacar : "))
    
     excedeu_saldo = sacar > Saldo

     excedeu_limite = sacar > limite

     excedeu_saques = numero_de_saques >= limite_de_saque

     if excedeu_saldo:
       print("Infelizmente não pôde ser realizado o saque, pois não possui saldo suficiente.")
    
     elif excedeu_limite:
       print("O valor de saque desejado excedi o limite, tente outro valor.")
    
     elif excedeu_saques:
       print("Você já utilizou o seu limite de saque, infelizmente não vai poder realizar outra operação.")
    
     elif sacar > 0:
        Saldo -= sacar
        Extrato += f"Saque: R$ {sacar:.2f}\n"
        numero_de_saques += 1
     else:
         print("❌Operação falhou o valor informado é inválido tente novamente.❌")

  elif opcao == "3":
   print("\n=============EXTRATO===============")
   print("Não foi realizado uma transação."if not Extrato else Extrato)
   print(f"\nSaldo: R$ {Saldo:.2f}")  
   print("======================================")

  elif opcao == "4" :
    break
  
  else:
     print("❌Opção inválida, tente novamente selecione outra opção!❌")

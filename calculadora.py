def calculadora():
  num1 = float(input("Digite o primeiro número"));
  num2 = float(input("Digite o segundo número"));
  operacao = input("Escolha a operação: +, -, *, /");

if(operacao == "+"):
    soma = num1 + num2;
    print(soma);
elif(operacao == "-"):
    sub = num1 - num2;
    print(sub);
elif(operacao == "*"):
    mult = num1 * num2;
    print(mult);
elif(operacao == '/'):
    if (num2 !=0):
      div = num1 / num2;
      print(div);
    else:
      print ("Digitar número diferente de zero")
  return calculadora()


calculadora();
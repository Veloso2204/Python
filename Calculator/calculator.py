# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y


print("Seleciona uma Operação.")
print("1.Adição")
print("2.Subração")
print("3.Multiplicação")
print("4.Divizão")

while True:
    # take input from the user
    choice = input("Selecione uma opção(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Insira o primeiro número: "))
            num2 = float(input("Insira o segundo número: "))
        except ValueError:
            print("Número Inválido. Mete um número válido.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Vamos fazer a próxima conta? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")
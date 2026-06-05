print("Exemplo de captura de exceções")

try:
    numero = int(input("Digite um número inteiro: "))
    resultado = 10 / numero
    
# Mostra o erro sem interromper o programa
except ValueError as e:
    print("Erro: Você deve digitar um número inteiro.")
    raise ValueError("Tipos de variáveis incompatíveis. Certifique-se de fornecer um número inteiro.") # Interrompe o programa

except ZeroDivisionError as e:
    print("Erro: Não é possível dividir por zero.")
        
except Exception as e:
    print(f"Erro: {e}")

else:
    print(f"Resultado da divisão: {resultado}")

finally: # Independente de ocorrer um erro ou não, o código dentro do bloco finally será executado
    print("Operação finalizada.")

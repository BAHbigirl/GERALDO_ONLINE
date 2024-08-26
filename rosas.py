#
## converter temperaturas
#

input("ola, ola!!! vamos converter??")
print('escolha uma das opcoes a seguir:')
print('de grau celsius para fahrenheit = 1')
print('de grau celsius para kelvin = 2')
print('de fahrenheit pra kelvin = 3')
print('de kelvin para celsiu = 4')
escolha= int(input("digite a letra da opção:"))

num=float(input("digite o grau a ser convertido:"))

if escolha == 1:
    CF= num *9/5 + 32
    print(CF)

elif escolha == 2:
    CK=num +273
    print(CK)

elif escolha == 3:
    FK=num - 273
    print(FK)

elif escolha == 4:
    KC= num - 273
    print(KC)


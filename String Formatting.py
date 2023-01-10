def print_formatted(number):
    # your code goes here
    binario_final = format(n, 'b')
    digitos = len(str(binario_final))
    for numero in range(1, n+1):
        decimal = format(numero, 'd')
        octal = format(numero, 'o')
        hexadecimal = format(numero, 'X')
        binario = format(numero, 'b')
        print(f'{decimal :>{digitos}} {octal :>{digitos}} {hexadecimal :>{digitos}} {binario :>{digitos}}')


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

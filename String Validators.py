if __name__ == '__main__':
    s = input()
    checks = ['isalnum', 'isalpha', 'isnumeric', 'islower', 'isupper']
    for check in checks:
        contador = 0
        for caracter in s:
            if getattr(caracter, check)():
                contador += 1
        print(contador > 0)

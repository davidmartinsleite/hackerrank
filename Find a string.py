def count_substring(string, sub_string):
    contagem = 0
    posicao = string.find(sub_string)
    while posicao != -1:
        contagem += 1
        posicao = string.find(sub_string, posicao+1)
    return contagem


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)

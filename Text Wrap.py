# parágrafo de entrada de forma que cada linha no parágrafo tenha
# no máximo caracteres de largura. O método wrap retorna uma lista
# de linhas de saída. A lista retornada está vazia se a saída agrupada
# não tiver conteúdo. A largura padrão é considerada 4.


import textwrap


def wrap(string, max_width):
    return textwrap.fill(string, width=max_width)


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

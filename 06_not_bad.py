"""
06. not_bad

Dada uma string, encontre a primeira aparição das
substrings 'not' e 'bad'. Se 'bad' aparecer depois
de 'not', troque todo o trecho entre 'not' e 'bad'
por 'good' e retorne a string resultante.

Exemplo: 'The dinner is not that bad!' retorna 'The dinner is good!'
"""

def not_bad(s):
    splited = s.split()
    p = ''
    if splited[-1][-1] in ':.;!?':
        p = splited[-1][-1]
        splited[-1] = splited[-1][:-1]
    if 'bad' in splited and 'not' in splited:
        n_index = splited.index('not')
        b_index = splited.index('bad')
        if n_index < b_index:
            s = " ".join(splited[:n_index] + ['good'] + splited[b_index+1:]) + p
    return s


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}({in_!r}) retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(not_bad, 'This movie is not so bad', 'This movie is good')
    test(not_bad, 'This dinner is not that bad!', 'This dinner is good!')
    test(not_bad, 'This tea is not hot', 'This tea is not hot')
    test(not_bad, "It's bad yet not", "It's bad yet not")
    test(not_bad, 'Is this movie not so bad?', 'Is this movie good?')
    test(not_bad, "It's can be bad, but is not so bad", "It's can be bad, but is good")

from app.funcao_print import funcao_print


def test_funcao_print():
    saida = funcao_print()
    gabarito = "Hello, World!"
    assert saida == gabarito
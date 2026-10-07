import pandera as pa
from pandera import DataFrameSchema, SchemaModel, Column, Check, Index, MultiIndex
from pandera.typing import Series
from datetime import date


class CadastroSchema(pa.SchemaModel):
    """
    Contrato de qualidade para os dados de cadastros.

    O schema define a estrutura esperada para o DataFrame extraído da tabela
    `cadastros`. Cada registro deve conter dados de identificação, localização,
    contato e datas de nascimento e cadastro.

    Colunas esperadas:
        id: identificador do cadastro.
        nome: nome da pessoa cadastrada.
        data_nascimento: data de nascimento.
        cpf: CPF da pessoa cadastrada.
        cep: código postal do endereço.
        cidade: cidade de residência.
        estado: estado de residência.
        pais: país de residência.
        genero: gênero informado.
        telefone: telefone de contato.
        email: endereço de e-mail.
        data_cadastro: data de criação do cadastro.

    Regras:
        - O índice deve ser inteiro e não nulo.
        - Campos textuais são tratados como strings.
        - Campos de data são tratados como datas.
        - A opção `coerce=True` permite ao Pandera converter valores para os
          tipos esperados antes da validação.
    """

    id: Series[str]
    nome: Series[str]
    data_nascimento: Series[date]
    cpf: Series[str]
    cep: Series[str]
    cidade: Series[str]
    estado: Series[str]
    pais: Series[str]
    genero: Series[str]
    telefone: Series[str]
    email: Series[str]
    data_cadastro: Series[date]

    index: Index[int]

    class Config:
        coerce = True
        strict = True

"""
A resposta que está no enunciado está bastante completa, de maneira mais
resumida:
    - Entre os métodos discutidos na UC, o de Simpson é o que apresenta maior
    precisão, pois substitui a curva por uma parábola e não por uma corda no
    intervalo considerado. Assim, garante-se, geralmente, um ajuste mais
    correto à função.
    - O método dos trapézios é um método de segunda ordem pois o erro varia com
    o quadrado do passo de integração.
    - O método de Simpson é um método de quarta ordem pois o erro varia com a
    quarta potência do passo de integração.
    - Para além do passo o erro também é influenciado pela própria integranda,
    o parametro ξ incontrolável.
    - Para estimar o erro, deve-se calcular o integral com o método escolhido
    variando o h.
    - Para garantir a validade do erro calculado, é necessário garantir que o
    valor de h é suficientemente pequeno. Essa garantia é obtida calculando o
    quoeficiente de convergência.
    - Depois de establecer qual o h para o qual o QC se adequa à ordem do
    método, deve-se ajustar h ao erro máximo pretendido.
"""

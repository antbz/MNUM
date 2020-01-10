"""
1. A soma acumulada de números inteiros tem pouca suscetibilidade a erros de
arredeondamento, o que aumenta a fiabilidade dos resultados, contudo,
como só é possível iterar em intervalos inteiros, a definição dos resultados
está limitada.

2. A soma acumulada de números em vírgula flutuante tem muita propensão a
erros de arredondamento, devido aos sucessivos arredondamentos da mantissa.
Tem a vantagem de permitir obter resultados mais granulares do que o iterador
1, mas a desvantagem de uma considerável perda de precisão à medida que o
número de iterações aumenta.

3. Neste iterador são somados, à semelhança do iterados 2, números em vírgula
flutuante, no entanto, esta não é uma soma acumulada. O valor a somar ao valor
inicial é atualizado por meio de uma multiplicação com um inteiro, o que
diminui o erro cometido pela acumulação de somas. Assim, este iterador
apresenta a vantagem de permitir maior granularidade que 1 e maior precisão que
2, mas a desvantagem de continuar suscetível a alguns erros na soma de VF.
Por exemplo, no caso em que as ordens de grandeza de x0 e h são muito díspares,
o resultado da adição poderia simplesmente ser igual ao maior dos dois números.

4. Este iterador é tão suscetível a erros como o 2. É efetuada uma soma
acumulada de números em vírgula flutuante. Como a fração exponenciada tem
representação absoluta em binário, desta operação não são criados mais erros do
que se a soma fosse acumulando um valor constante. No entanto, como este valor
é decrescente, quando atingir uma ordem de grandeza muito menor do que xn, a
precisão do resultado da adição será prejudicada, sendo que no pior caso o
valor do iterador deixa de variar. Tem como vantagem permitir variar o valor do
iterador de uma maneira que pode ser útil, mas a desvantagem de se
realizarem muitas operações com vírgula flutuante e de as ordens de grandeza
dos números se afastarem progressivamente.
"""

"""
O método númerico mais adequado é o de Levenberg-Marquardt.

Este método é uma combinação do método do gradiente com o método da quádrica.
Assim, colmata os problemas de um dos métodos com as vantagens do outro,
aliando o melhor desempenho do método da quádrica na vizinhança, extendendo a
sua aplicabilidade para lá da vizinhança deste. Também é um método que lida
bem com depressões alongadas, já que a quádrica permite detetar esse
alongamento. Esse caso verifica-se nesta função.

???Outra situação complicada que surge no caso apresentado é o da proximidade
entre mínimos. O método irá convergir para um deles, no entanto este pode não
ser o menor ou ter características que não se aplicam ao contexto mais alargado
do problema. Para combater isso seria necessário definir constrições a aplicar
ao método de modo a "forçar" a convergência para o mínimo pretendido.???
{don't quote me on this}
"""

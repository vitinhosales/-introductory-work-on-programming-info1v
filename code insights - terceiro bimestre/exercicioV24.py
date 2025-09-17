# @cikey 8ac9e6fe4b013542d94d7c7ce2899e6c
# @sid 20251174010072
# @aid V2.4


#begin_inputs
valor_compra = int(input("Digite o valor da sua compra:"))

#end_inputs

avista = int(valor_compra - valor_compra * 9/100)
print(avista)

prestacao_5x = int(valor_compra/5)
print(prestacao_5x)

prestacao_10x = int((valor_compra + valor_compra * 17/100)/10)
print(prestacao_10x)
# @cikey 8ac9e6fe4b013542d94d7c7ce2899e6c
# @sid 20251174010072
# @aid V2.4


#begin_inputs
valor_compra = int(input("Digite o valor da sua compra:"))

#end_inputs

a_vista = valor_compra - valor_compra * 0.09

parcelado_5x = valor_compra / 5

parcelado_com_juros = valor_compra + valor_compra * 0.17
parcelado_10x = parcelado_com_juros / 10

print("{}".format(a_vista))
print("{}".format(parcelado_5x))
print("{}".format(parcelado_10x))
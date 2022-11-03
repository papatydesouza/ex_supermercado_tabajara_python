print("***** SEJA BEM VINDO AO SUPERMERCADO TABAJARA ******")
cartao_tabajara = input("Você possui cartão tabajara?\n Digite S-sim ou N-não\n")

tipo_carne_str = input("Qual será a sua escolha de carne?\n1-Filé\n2-Alcatra\n3-Picanha\n")
quantidade_carne_str = input("Qual será a quantidade de carne? Digite o valor em gramas!\n")
tipo_carne = int(tipo_carne_str)
quantidade_carne = int(quantidade_carne_str)

if (tipo_carne == 1 and quantidade_carne < 5000):
    valor_total = (quantidade_carne * 5)/1000
elif (tipo_carne == 1 and quantidade_carne > 5000):
    valor_total = (quantidade_carne * 6)/1000
elif (tipo_carne == 2 and quantidade_carne < 5000):
    valor_total = (quantidade_carne * 6)/1000
elif (tipo_carne == 2 and quantidade_carne > 5000):
    valor_total = (quantidade_carne * 7)/1000
elif (tipo_carne == 3 and quantidade_carne < 5000):
    valor_total = (quantidade_carne * 7)/1000
elif (tipo_carne == 3 and quantidade_carne > 5000):
    valor_total = (quantidade_carne * 8)/1000


if (cartao_tabajara == "S"):
    valor_final = ((valor_total * 95) /100)

print("****** CUPOM FISCAL DA COMPRA *******")
print("Tipo de Carne Escolhido: {}\nQuantidade de Carne: {}\nPreço Total: R${}\nPago com Cartão Tabajara: {}\nValor total com Desconto: R${}" .format(tipo_carne,quantidade_carne,valor_total, cartao_tabajara, valor_final))

print("******* FIM DO CUPOM FISCAL *******")
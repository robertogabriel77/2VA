vt = float(input("Qual o valor total da compra? "))
vp = float(input("Qual o valor pago? "))
troco = vp-vt
falta = vt-vp
if vp < vt:
    print(f"Valor pago insuficiente,faltam {falta}.")
elif vp==vt:
    print(f"Sem troco.")
else:
    print(f"O valor do troco é {troco}")

def preco_final(preco,desconto):
    preco_final = preco * (1-desconto/100)
    return print(f"preço final do produto é {preco_final}")

if __name__ == "__main__":
    preco = int(input("Diga o preço do produto: "))
    desconto = int(input("Diga de quantos porcento é o desconto: "))

    preco_final(preco,desconto)
header = "Price list\n"
product_prices = {"Tomatoes":1.75, "Bananas":2.25, "Oranges":3}

fout = open("pricelist.txt", "w")
if not fout.write(header):
    print("mislukt")

temp = list(product_prices)
temp.sort()
for key in temp:
    print(key, temp[key])
fout.close()
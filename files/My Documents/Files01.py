header = "Price list\n"
product_prices = {"Tomatoes":1.75, "Bananas":2.25, "Oranges":3}

fout = open("pricelist.txt", "w")
print(fout.write(header))
fout.write(str(product_prices))
fout.close()



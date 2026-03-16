wish = "Hurrah!"

def salvo(n, message):
    print(message)
    salvo(n-1, message)
    
salvo (10, wish)


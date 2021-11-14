print("Welcome in Luigi's store!")
try:
    product_name=str(input("Write the product name: "))
    print(product_name, type(product_name))
except:
    print("Process interrupted. Bad data type")
    exit()

try:
    product_pricenet=float(input("Write the product price net: "))
    print(product_pricenet, type(product_pricenet))
except:
    print("Process interrupted. Bad data type")
    exit()

tax=0.23
product_gross=(product_pricenet*tax)+product_pricenet
print("The price with taxess (+23%) will be:")
print(product_gross)

try:
    client_mail=str(input("Write the client mail: "))
    print(client_mail, type(client_mail))
except:
    print("Process interrupted. Bad data type")
    exit()

try:
    client_phone=int(input("Write the client phone number: "))
    print(client_phone, type(client_phone))
except:
    print("Process interrupted. Bad data type")
    exit()

label=("name", "net price", "gross price", "mail", "phone")

print("Your basket: ")
print(label)
basket=(product_name, product_pricenet, product_gross, client_mail, client_phone)
print(basket)
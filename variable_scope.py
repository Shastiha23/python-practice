name="priya" #global vari
def order():
    food="pizza" #local vari
    print("order name:",name)
    print("your order is:",food)
order()
def order_id():
    id=103 #enclosing
    print("order is confirmed")
    def details():
        print("id:",id,"  name:",name)
    details()
order_id()



        

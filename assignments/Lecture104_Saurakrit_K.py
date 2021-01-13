class Customer:
    name = ""
    lastName = ""
    age = 0

    def addCart(self):
        print("Added to %s %s 's cart" %(self.name,self.lastName))

customer1 = Customer()
customer1.name = "Saurakrit"
customer1.lastName = "Klinmali"
customer1.addCart()

customer2 = Customer()
customer2.name = "Killua"
customer2.lastName = "Zoldyck"
customer2.addCart()

customer3 = Customer()
customer3.name = "Roronoa"
customer3.lastName = "Zoro"
customer3.addCart()
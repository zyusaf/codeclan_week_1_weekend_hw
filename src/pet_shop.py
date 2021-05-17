# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, cash):
    pet_shop["admin"]["total_cash"] += cash

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, num_sold):
    pet_shop["admin"]["pets_sold"] += num_sold

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, breed_info):
    pets = pet_shop["pets"]
    pets_by_breed = []
    for pet in pets:
        if pet["breed"] == breed_info:
            pets_by_breed.append(pet)
    
    return pets_by_breed

def find_pet_by_name(pet_shop, name):
    pets = pet_shop["pets"]
    for pet in pets:
        if pet["name"] == name:
            return pet

def remove_pet_by_name(pet_shop, name):
    pets = pet_shop["pets"]
    for pet in pets:
        if pet["name"] == name:
            pets.remove(pet)

def add_pet_to_stock(pet_shop, add_pet):
    pets = pet_shop["pets"]
    pets.append(add_pet)

def get_customer_cash(customers):
    return customers["cash"]

def remove_customer_cash(customers, cash):
    customers["cash"] -= cash

def get_customer_pet_count(customers):
    return len(customers["pets"])

def add_pet_to_customer(customers, add_pet):
    pets = customers["pets"]
    pets.append(add_pet)

def customer_can_afford_pet(customers, new_pet):
    return customers["cash"] >= new_pet["price"]

# def sell_pet_to_customer(pet_shop, pet, customer):

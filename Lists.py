cheky = []

def show_food():
    """Функція виводить поточний список"""
    print("Список фруктів:", cheky)

def add_food():
    cheky.append(food)
    print(f"Успішно додано: {food}")
while True:
    food = input("Що додати до списку або 'exit': ")

    if food.lower() == 'exit':
        print(f"Список: {cheky}")
        input()
        break
    else:
        add_food()
        show_food()
#Код сам написав




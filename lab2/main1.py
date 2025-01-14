def greet(name):
    return f"Привет, {name}!"
def square(number):
    return int(number) ** 2
def max_of_two(x,y):
    if x > y:
        return f"Большее число: {x}."
    elif x < y:
        return f"Большее число: {y}."
    else:
        return f"Числа равны"


print(greet("Александр"))
print(square(4))
print(max_of_two(5,5))

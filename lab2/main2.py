def describe_person(name, age=30):
    return f"Имя:{name} Возраст:{age}"


print(describe_person("Ваня", 10))
print(describe_person("Ваня"))

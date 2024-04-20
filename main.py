
#Homework 2
cats = ["Murzik", "Barsik", "Pantera"]
print(*cats, sep=", ")

#Homework 3
countries_names = ['Ukraine', 'Spain', 'Italy']
countries_capitals = {
    countries_names[0]:'Kyiv',
    countries_names[1]:'Madrid',
    countries_names[2]:'Rome'
}
print(f"{countries_names[0]}: {countries_capitals[countries_names[0]]}")
print(f"{countries_names[1]}: {countries_capitals[countries_names[1]]}")
print(f"{countries_names[2]}: {countries_capitals[countries_names[2]]}")

#Homework 4
a = input("Enter a: ")
b = input("Enter b: ")
print(f"{a} + {b} = {int(a)+(int(b))}")
print(f"{a} * {b} = {int(a)*(int(b))}")

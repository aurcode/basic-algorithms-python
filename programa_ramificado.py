name_1 = input("¿Como se llama usted?: ")
age_1 = int(input("¿Cuantos años tiene?: "))
name_2 = input("¿Como se llama su amigo?: ")
age_2 = int(input("¿Cuantos años tiene su amigo?: "))


if age_1 > age_2:
    print(f"{name_1} es mayor que {name_2}.")
elif age_1 < age_2:
    print(f"{name_2} es mayor que {name_1}.")
else:
    print(f"{name_1} y {name_2} son de la misma edad.")

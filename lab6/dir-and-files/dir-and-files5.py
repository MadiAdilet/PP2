import os


zxc = ["LADA", "BMW", "Mersedes", "Porche", "Toyota"]


with open("aa.txt", "a") as name:
    for i in zxc:
        name.write(f'{i}\n\t')
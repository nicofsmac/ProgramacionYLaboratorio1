import re

texto = "hola y 2455chau"

print(re.split(" [y] [0-9]+", texto))



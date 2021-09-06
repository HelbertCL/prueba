a=float(input("ingrese numero de mujeres: "))
b=float(input("ingrese numero de hombres: "))
total=a+b
mujeres=round(a/total,2)
hombres=round(b/total,2)
print("el porcentaje de mujeres es: ",mujeres,"el porcentaje de hombres es: ",hombres,sep="\n")

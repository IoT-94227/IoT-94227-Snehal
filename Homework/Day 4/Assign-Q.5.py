conversions = [
   # t_to_kg 
   lambda t: t * 1000,                    
   # kg_to_gm 
   lambda kg: kg * 1000,                  
   # gm_to_mg 
   lambda g: g * 1000,                    
   # mg_to_pounds 
   lambda mg: mg * 0.00000220462262       
]

tonns = float(input("Enter weight in tonns: "))

kg= conversions[0](tonns)
gm= conversions[1](kg)
mg= conversions[2](gm)
lbs=conversions[3](mg)

print("---Weight conversions---")
print(f"{kg} kg")
print(f"{gm} gm")
print(f"{mg} mg")
print(f"{lbs} lbs")


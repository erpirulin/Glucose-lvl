# El nivel de glucosa es una entrada para este software
glucose_level = int(input())

# Mostrar mensaje si el nivel de glucosa es menor a 70
if glucose_level < 70:
  print("Low glucose level")


# Mostrar mensaje si el nivel de glucosa es mayor a 140
elif glucose_level > 140:
  print("High glucose level")

# Mostrar mensaje si no se cumplen ninguna de las condiciones anteriores
else:
  print("Normal range")

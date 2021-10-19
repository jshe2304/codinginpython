import random

def get_temperature():
  temperature = random.randint(70, 90)

  return temperature

temperature = get_temperature()

while temperature > 80:

  print (temperature)
  print ('Fan is on!')

  temperature = get_temperature()

print (temperature)

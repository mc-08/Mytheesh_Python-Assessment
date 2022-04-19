#Question 5:
#Weight of people in kg
WeightOnEarth = {'John':45, 'Shelly':65, 'Marry':35}
# Gravitational force on the Moon:
GMoon = 1.622
# Gravitational force on the Earth:
GEarth = 9.81
for wEarth in WeightOnEarth:
  wMoon =map(int,lambda a :(wEarth*GMoon)/GEarth)

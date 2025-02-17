import math

order_belt = {'Branca': 0,
              'Amarela': 1,
              'Verde': 2,
              'Azul': 3,
              'Roxa': 4,
              'Marrom': 5,
              'Preta': 6,
              'Vermelha': 7
            }

def calculate_lessons_to_upgrade(n):
  d = 1.47
  k = 40 / math.log(d)
  aulas = k * math.log(n + d)
  return round(aulas)

import math
from math import pi, sin, cos

ang = float(input('\n Digite ângulo em graus: '))
rang = ang * pi/180

if (rang > pi / 2 and rang <= pi) or (rang > 3 * pi / 2 and rang <= 2 * pi):
    print('\n Seno: ', sin(rang))
else:
    print('\n Co-seno: ', cos(rang))

print('\n')
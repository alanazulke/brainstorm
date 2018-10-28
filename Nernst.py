from numpy import log
import matplotlib.pyplot as plt

e0 = 2
R = 8.34
T = 298.15
z = 1
F = 96500
output = list()
x = list()

for Q in range(0, 500, 1):
    e = e0 - (R*T/(z*F))*log(Q)
    print(e)
    output.append(e)
    x.append(log(Q))
plt.plot(output, x)
plt.ylabel('E/V')
plt.show()
print('finish')








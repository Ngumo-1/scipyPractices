import numpy as np
from optimize import minimizeFunc
from interpolate import linear_interp, cubic_interp, quadratic_interp
import matplotlib.pyplot as plt

# def eqn(params, args):
#     a,b,c,d,e,f=params
#     x,y=args
#     return a * x**2 + b * y**2 + c * x * y + d * x + e * y + f
#
# args=(1, 2)
#
# initial_guess=[0,0,0,0,0,0]
#
# optimized_constants=minimizeFunc(eqn, initial_guess, args)
#
# print("Optimized constants: ", optimized_constants)

x = np.linspace(0, 10, 10)
y = np.sin(x) + np.random.normal(0, 0.2, len(x))

lin_interp=linear_interp(x, y)
cub_interp=cubic_interp(x,y)
quad_interp=quadratic_interp(x,y)

x_fine = np.linspace(0, 10, 100)

plt.scatter(x, y, label="Original points")

plt.plot(x_fine, lin_interp(x_fine), label="Linear Interpolation")
plt.plot(x_fine, cub_interp(x_fine), label="Cubic Interpolation")
plt.plot(x_fine, quad_interp(x_fine), label="Quadratic Interpolation")

plt.title('Interpolation and Visualization')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()
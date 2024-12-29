import numpy as np
import matplotlib.pyplot as plt
# 이산적인 데이터 (x와 y 값)

y_discrete = np.array([0, 0, 100, 200, 200, 300, 400, 500, 500, 600, 600, 700, 700, 700, 800, 800, 800, 900, 900, 1000, 1100, 1100, 1200, 1300, 1300, 1400, 1400, 1500, 1600, 1600, 1600, 1600, 1600, 1700, 1700, 1800, 1800, 1900, 1900, 2000, 2000, 2100, 2100, 2200, 2200, 2300, 2300, 2400, 2400, 2500, 2500, 2600, 2600, 2700, 2800, 2800, 2900, 3000, 3000, 3000, 3000])
x_discrete = np.array(range(0, len(y_discrete)))
# 3차 스플라인 보간법
coefficients = np.polyfit(x_discrete, y_discrete, deg=3)
polynomial = np.poly1d(coefficients)

# 스플라인 보간법의 미분 (1차 미분)
polynomial_derivative = polynomial.deriv()
polynomial_derivative2 = polynomial_derivative.deriv()

critical_points = np.roots(polynomial_derivative2)
extreme_value = polynomial_derivative(critical_points[0])


# 연속적인 x 값 생성
x_continuous = np.linspace(0, len(x_discrete), 1000000)

y_continuous = polynomial(x_continuous)

# 1차 미분된 값 계산
y_derivative = polynomial_derivative(x_continuous)

# 그래프 출력
plt.plot(x_discrete, y_discrete, 'o', label='S(t)')
plt.plot(x_continuous, y_continuous, '-', label='F(t)')
plt.plot(x_continuous, y_derivative, '--', label='F`(t)')
plt.legend()
plt.show()

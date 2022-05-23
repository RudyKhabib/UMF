import matplotlib.pyplot as plt
import numpy as np

x_max = 1
t_max = 0.5


def fu_an(t_f):
    global x_max
    global t_max
    n_x = 1000
    h = x_max / n_x
    u_an = np.zeros(n_x + 1)
    u_f = u_nachalni(n_x)
    for b in range(len(u_f)):
        if h * b < t_f:
            u_an[b] = 0
        else:
            u_an[b] = u_f[int((b * h - t_f) * n_x)]
    return u_an


def formula(u_ff, i_f, h_f, t_f):
    return u_ff[i_f] - (t_f / h_f) * (u_ff[i_f] - u_ff[i_f - 1])


def u_nachalni(n_x_nachalni):
    global x_max
    x_nch = np.linspace(0, x_max, n_x_nachalni + 1)
    u_nch = np.zeros(n_x_nachalni + 1)
    for i_n, value_n in enumerate(x_nch, 0):
        if 0.1 < value_n <= 0.2:
            u_nch[i_n] = 1
    return u_nch


def calculation(nya):
    global x_max
    global t_max
    v = np.zeros(nya + 1)
    hc = x_max / nya
    tc = t_max / nya
    u = u_nachalni(nya)
    u_new = np.zeros(nya + 1)
    for j in range(1, nya + 1):
        u_new[0] = v[j]
        for i in range(1, nya + 1):
            u_new[i] = formula(u, i, hc, tc)
        for i in range(nya + 1):
            u[i] = u_new[i]
    return u


n_100 = 100
n_200 = 200
n_500 = 500
n_1000 = 1000
n_2000 = 2000
n_5000 = 5000
n_10000 = 10000
x = np.linspace(0, 1, 1000 + 1)
x_100 = np.linspace(0, 1, n_100 + 1)
x_200 = np.linspace(0, 1, n_200 + 1)
x_500 = np.linspace(0, 1, n_500 + 1)
x_1000 = np.linspace(0, 1, n_1000 + 1)
x_2000 = np.linspace(0, 1, n_2000 + 1)
x_5000 = np.linspace(0, 1, n_5000 + 1)
x_10000 = np.linspace(0, 1, n_10000 + 1)
uan = fu_an(t_max)
u_100 = calculation(n_100)
u_200 = calculation(n_200)
u_500 = calculation(n_500)
u_1000 = calculation(n_1000)
u_2000 = calculation(n_2000)
u_5000 = calculation(n_5000)
u_10000 = calculation(n_10000)
plt.title('Linear advection')
plt.xlabel('x coordinate')
plt.ylabel('function value')
plt.grid()
plt.plot(x_100, u_100, x_200, u_200, x_500, u_500, x_1000, u_1000, x_2000, u_2000, x_5000, u_5000, x_10000, u_10000, x,
         uan)
plt.show()

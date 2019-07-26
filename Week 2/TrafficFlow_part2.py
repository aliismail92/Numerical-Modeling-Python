import numpy
import sympy
from matplotlib import pyplot
%matplotlib inline

vm = 136
L = 11
pm = 250
nx = 51
dt = 0.001
dx = L/(nx-1)

x = numpy.linspace(0,L, nx)
rho0 = numpy.ones(nx)*20
rho0[10:20] = 50

def get_rho(rho0, nt):
    nt = nt
    rho = rho0.copy()
    for n in range (nt):
        rho[0] = 20
        rho[1:] = rho[1:] - dt/dx * vm*(1 - 2/pm * rho[1:]) * (rho[1:] - rho[:-1])
    return rho

#1st question at t = 0

v = numpy.zeros(51)
for i in range(51):
    v[i] = vm * (1-rho0[i]/pm)
v.min()/3.6

#2nd question At time 3 min nt  = 50 (3/60/0.001)
get_rho(rho0, 50)

v = numpy.zeros(51)
for i in range(51):
    v[i] = vm * (1-rho[i]/pm)
v.mean()/3.6

#3rd question at time 6min

v.min()/3.6

""" 
pyplot.figure(figsize=(6.0, 4.0))
pyplot.xlabel('x')
pyplot.ylabel('rho')
pyplot.grid()
pyplot.plot(x, rho0, label='Initial',
            color='C0', linestyle='--', linewidth=2)
pyplot.plot(x, rho, label='nt = {}'.format(nt),
            color='C1', linestyle='-', linewidth=2)
pyplot.legend(loc='upper right')
pyplot.xlim(0.0, L)
pyplot.ylim(5, 55); """
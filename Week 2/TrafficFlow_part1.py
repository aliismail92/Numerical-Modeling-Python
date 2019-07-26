import numpy
import sympy
from matplotlib import pyplot
%matplotlib inline

vm = 80
L = 11
pm = 250
nx = 51
dt = 0.001
dx = L/(nx-1)

x = numpy.linspace(0,L, nx)
rho0 = numpy.ones(nx)*10
rho0[10:20] = 50

def get_rho(rho0, nt):
    nt = nt
    rho = rho0.copy()
    for n in range (nt):
        rho[0] = 10
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
get_rho(rho0, 100)

v = numpy.zeros(51)
for i in range(51):
    v[i] = vm * (1-rho[i]/pm)
v.min()/3.6
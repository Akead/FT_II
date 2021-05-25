import numpy

Fs = 5e3
Fg = 1.6e3

#Fs=45*1e3
#Fg=12.35*1e3

pi = numpy.pi

def a():
    return 2*Fs

def b(omega):
    return 2*numpy.sqrt(2)*Fs*numpy.tan(omega/(2*Fs))

def c(omega):
    return (2*Fs*numpy.tan(omega/(2*Fs)))**2

omega = 2*pi*Fg

a = a()
b = b(omega)
c = c(omega)

print(f'a = {a}')
print(f'b = {b}')
print(f'c = {c}')

def b_0():
    return c/(a**2 + a*b + c)

def b_1():
    return 2*c/(a**2 + a*b + c)

def b_2():
    return c/(a**2 + a*b + c)

def a_1():
    return -(2*c - 2*a**2)/(a**2+a*b+c)

def a_2():
    return -(a**2 + c - a*b)/(a**2 + a*b + c)

b_0 = b_0()
b_1 = b_1()
b_2 = b_2()

a_1 = a_1()
a_2 = a_2()

print(f'b(0) = {b_0}')
print(f'b(1) = {b_1}')
print(f'b(2) = {b_2}')

print(f'a(1) = {a_1}')
print(f'a(2) = {a_2}')

import numpy as np

def sphere1(x):
    """y=(x0 - 1)^2 + (x1 - 2)^2 + (x2 - 3)^2"""
    return (x[0] - 1)**2 + (x[1] - 2)**2 + (x[2] - 3)**2 + 10 

def sphere2(x):
    """y=(x0 + 1)^2 + (x1 - 1)^2"""
    return (x[0] + 1)**2 + (x[1] - 1)**2 + 5

def sphere3(x):
    """y=(x0 + 1)^2 + (x1 - 1)^2 + (x2 - 3)^2 + 6"""
    return (x[0] + 1)**2 + (x[1] - 1)**2 + (x[2] - 6)**2 + 6

def sphere4(x):
    """y = sum_{i = 0}^20 (xi - 4)^2"""
    return np.sum((x - 4)**2) + 123

def beale(x):
    """y = (1.5-x0+x0x1)^2 + (2.25-x0+x0x1^2)^2 + (2.625-x0+x0x1^3)^2"""
    return (1.5 - x[0] + x[0]*x[1])**2 \
        +  (2.25 - x[0] + x[0]*(x[1] ** 2))**2 \
        +  (2.625 - x[0] + x[0]*(x[1] ** 3))**2

def levi(x):
    """y = sin^2(3pi*x0) + (x0-1)^2 * (1+sin^2(3pi*x1)) + (x1-1)^2 * (1+sin^2(2pi*x1))"""
    return np.sin(3*np.pi*x[0])**2 \
    + (x[0]-1)**2 * (1 + np.sin(3*np.pi*x[1])**2) \
    + (x[1]-1)**2 * (1 + np.sin(2*np.pi*x[1])**2)
    
def schaffer_n4(x):
    return 0.5 + (np.cos(np.sin(np.abs(x[0]**2 - x[1]**2))) ** 2 - 0.5) \
        /  ((1 + 0.001*(x[0]**2 + x[1]**2)) ** 2)
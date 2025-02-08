import numpy as np


def f1(x: np.ndarray) -> np.ndarray:
    return np.sin(x[0])

def f2(x: np.ndarray) -> np.ndarray: 
    return (x[0] * np.cosh(((np.cos((x[0] / 4.0000)) + 7.0000) + 7.0000)))

def f3(x: np.ndarray) -> np.ndarray:
    return np.subtract(np.add(np.subtract(np.multiply(np.multiply(x[0],x[0]),2),np.multiply(np.sinh(x[1]),2)),np.multiply(np.tanh(6.5153),4)),np.multiply(x[2],3))

def f4(x: np.ndarray) -> np.ndarray:
    return np.cosh(np.cosh((np.arctan(-3.2684) + np.divide(x[0],x[0])))) + np.sinh((np.cosh(np.cosh(np.cosh((np.arctan(-1.3125) + np.divide(x[0],x[0]))))) * np.tanh(np.cos(x[1])))) + (np.cosh((np.arctan(-1.8241) + (x[0] / 13.9523))) + np.sinh((np.cosh(np.cosh(np.arctan(-2.0000))) * np.tanh(np.cos(x[1])))))

def f5(x: np.ndarray) -> np.ndarray:
    return np.multiply(np.subtract(np.add(np.subtract(np.multiply(np.cosh(x[1]),np.sin(x[0])),np.cosh(x[1])),np.add(x[1],x[0])),np.tanh(np.subtract(np.add(x[1],x[0]),np.cosh(x[1])))),np.cos(np.arctan(np.sinh(np.sinh(-4.3606)))))

def f6(x: np.ndarray) -> np.ndarray:
    # return (1.6943887875521109 * x[1]) + ((-6.0562334247427 * x[0]) * np.abs(0.11473376637346892))
    return (((np.tanh(x[0]) + (x[1] - x[0])) - (x[1] / 5.3981)) + x[1])

def f7(x: np.ndarray) -> np.ndarray:
    return (np.cosh(np.exp(np.cos((x[1] - x[0])))) + ((np.exp((x[0] * x[1])) + np.cosh(np.exp(np.cos((x[1] - x[0]))))) * (x[1] * x[0])))

def f8(x: np.ndarray) -> np.ndarray: 
    return  ((np.sinh(x[5])) + np.multiply(x[5],7) - 6.7372) * np.abs((np.sinh(x[5])) + np.multiply(x[5],15))
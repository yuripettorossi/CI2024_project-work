import numpy as np


def f1(x: np.ndarray) -> np.ndarray:
    return np.sin(x[0])

def f2(x: np.ndarray) -> np.ndarray: 
    return (x[0] * np.cosh(((np.cos((x[0] / 4.0000)) + 7.0000) + 7.0000)))

def f3(x: np.ndarray) -> np.ndarray:
    return np.subtract(np.add(np.subtract(np.multiply(np.multiply(x[0],x[0]),2),np.multiply(np.sinh(x[1]),2)),np.multiply(np.tanh(6.5153),4)),np.multiply(x[2],3))

def f4(x: np.ndarray) -> np.ndarray:
    return ((3.22 * np.exp((np.cos(x[1]) * (np.tanh(1.99) * np.tanh((0.16 + np.cosh(1.04))))))) + ((np.tanh((0.27 + np.cosh(x[1]))) * ((np.tanh((2.62 + (3.69 + x[0]))) * (((np.tanh(((x[1] + np.exp(1.04)) + 3.56)) * np.tanh((x[1] + np.cosh(2.55)))) * 1.06) * np.tanh((0.52 + np.cosh(x[1]))))) * np.exp(np.cosh(np.tanh(x[1]))))) * np.cos(x[1])))
    # return np.multiply(np.add(np.cos(np.sinh(np.sinh(np.cos(x[1])))),np.sinh(np.sinh(np.sinh(np.cos(x[1]))))),np.add(np.sinh(np.sinh(np.cos(x[1]))),np.sinh(2.00)))

def f5(x: np.ndarray) -> np.ndarray:
    return (((((((np.log((np.cosh(np.sinh(x[0])) ** (np.log(np.cosh(x[0])) - np.log(np.cosh(x[0]))))) * x[0]) * x[0]) * x[0]) * x[0]) * x[0]) * x[0]) * x[0])

def f6(x: np.ndarray) -> np.ndarray:
    return (1.6943887875521109 * x[1]) + ((-6.0562334247427 * x[0]) * np.abs(0.11473376637346892))
    # return np.subtract(np.multiply(x[1],2.69),np.arctan(x[0]))

def f7(x: np.ndarray) -> np.ndarray:
    return (np.exp(x[0]) ** x[1]) + np.cos(np.abs(np.cosh(x[1]))) + np.cos(np.exp((np.exp(x[0]) ** x[1]))) + np.cos(np.cosh(x[0])) + ((np.cos(np.exp((np.exp(x[0]) ** x[1]))) + ((np.exp(x[0]) ** x[1]) + (np.exp(x[0]) ** x[1]))) + ((np.exp(x[0]) ** x[1]) + (np.exp(x[0]) ** x[1])))
  
def f8(x: np.ndarray) -> np.ndarray: 
    return  ((np.sinh(x[5])) + np.multiply(x[5],7) - 6.7372) * np.abs((np.sinh(x[5])) + np.multiply(x[5],15))
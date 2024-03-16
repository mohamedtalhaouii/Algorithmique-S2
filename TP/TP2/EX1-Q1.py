from math import sqrt

def fonction(x : float): # car (x ∈ ℝ)
    return (x**5) - abs(1 - sqrt(x**2)) + 1 / (1 + x**2)


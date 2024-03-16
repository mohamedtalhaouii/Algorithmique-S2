from math import sqrt

def fonction(x : float): # car (x ∈ ℝ)
    if x >= 0:
        return sqrt(x) + 2
    elif x < 0:
        return (-x)**5
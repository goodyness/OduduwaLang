import math

def apapo(atoye):
    """Calculate the sum of a list (apapo awọn nọmba)."""
    return sum(atoye)

def iwon(atoye):
    """Calculate the average/mean of a list (iwọn awọn nọmba)."""
    if not atoye:
        return 0
    return sum(atoye) / len(atoye)

def gbere_square(n):
    """Calculate the square root (gbere square nọmba)."""
    return math.sqrt(n)

def agbara(n, p):
    """Calculate n to the power of p (agbára nọmba)."""
    return math.pow(n, p)

def to_bi_ju(atoye):
    """Find the maximum value (eyi ti o tobi ju)."""
    return max(atoye)

def kere_ju(atoye):
    """Find the minimum value (eyi ti o kere ju)."""
    return min(atoye)

def se_ifosi(n):
    if (n == 1):
        return 1
    else:
        return (n * se_ifosi((n - 1)))
abajade = se_ifosi(5)
print('Abajade jẹ: ', abajade)
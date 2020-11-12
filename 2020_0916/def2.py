def postTaxPrice(price):
    ans = price * 1.08
    return ans

print(postTaxPrice(100),'円')
print(postTaxPrice(128),'円')
print(postTaxPrice(980),'円')


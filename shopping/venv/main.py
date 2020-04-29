from random import randint

from utilities.utils import multiply, divide
from shopping.more_shopping import shopping_cart

print(f'Shopping name: { __name__ }')

if __name__ != '__main__':
    print('I am not in main!')
    exit()

print('I am in main! \n')

cart = shopping_cart.buy('apple')
print(f'Cart: { cart }')

print(f'Multiply: { multiply(3, 2) }')
print(f'Divide: { divide(3, 2) }')
print(f'Random: { randint(0, 1) }')

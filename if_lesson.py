def discounted(price, discount, max_discount = 50, name = ''):
    price = abs(float(price))
    discount = abs(float(discount))
    max_discount = abs(float(max_discount))
    if max_discount > 99:
        raise ValueError('Максимальная скидка не может быть больше 99%')
    if discount >= max_discount or "iphone" in name.lower() or not name:
        price_with_discount = price
        
    else:
        price_with_discount = price - price * discount / 100
    return price_with_discount

def format_price(price):
    price = int(price)
    return f'Цена: {price} руб.'


stock = [
    {'name': 'Samsung Galaxy s10', 'stock': 8, 'price': 50000.0, 'discount': 15},
    {'name': 'iPhone Xs Plus', 'stock': 24, 'price': 65432.1, 'discount': 50},
	{'name': 'Б/У', 'stock': 18, 'price': 10000.0, 'discount': 10}
]

# product['with_discount'] = discounted(product['price'],product['discount'])

# print(discounted(100,40))

# test = format_price(56.24)
# print(test)

for phone in stock:
		phone["price_final"] = discounted(phone["price"], phone["discount"], name=phone["name"])
print(stock)

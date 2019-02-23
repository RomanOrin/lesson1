def get_summ (one, two, delimiter ='&'):
    return f'{one} {delimiter} {two}'

one1 = "Learn"
two1 = "Python"
print(get_summ(one1,two1))

def format_price(price):
    return f'Цена: {int(price)} рублей '
x=input()
print(format_price(x))

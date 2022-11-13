# TODO решить с помощью list comprehension и распечатать его
import pprint

list_ = []
count = 16
for number in range(count):
    list_.append(number)
cashier = [{'bin':bin(item), 'dec':(item),'hex':hex(item),'oct':oct(item)} for item in list_]
pprint.pprint(cashier)
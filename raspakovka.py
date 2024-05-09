def print_params (a = 1, b = 'строка', c = True):
    print(a,b,c)
    print(a)
    #print(c)
    #print()


print_params()
print_params(b=25,)
print_params(c=[1, 2, 3])

values_list = (888,'dog', False)
values_dict = {'a': 1,'b': 'точка','c': False}

print_params(*values_list )
print_params(**values_dict)

#3.2.1 
def do_twice(f):
    f()
    f()

def print_spam():
    print('spam')

do_twice(print_spam)

#3.2.2 
def do_twice_arg(f, value):
    f(value)
    f(value)

#3.2.3 
def print_twice(x):
    print(x)
    print(x)

#3.2.4 
do_twice_arg(print_twice, 'mensagem')

#3.2.5 
def do_four(f, value):
    do_twice_arg(f, value)
    do_twice_arg(f, value)

do_four(print_twice, 'spam')
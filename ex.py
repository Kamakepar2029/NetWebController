import functools

fn_list = {}


def integration(fn):
    if fn.__name__ not in fn_list.keys():
        fn_list[fn.__name__] = fn

    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        fn_list[fn.__name__](*args, **kwargs)

    return wrapper


def replace_fn(name, fn):
    fn_list[name] = fn


@integration
def test_1():
    print('Me')
    print("defef")


#def integration_1():
#    print('Lol')
#    print("replaced def 1")
#def integration_2():
#    print('Mu')
#    print("replaced def 2")

def control():
    print('hello')
replace_fn("test_1",control)
test_1()
#test_1()
#replace_fn("test_1", integration_1)
#test_1()
#replace_fn("test_1", integration_2)
#test_1()

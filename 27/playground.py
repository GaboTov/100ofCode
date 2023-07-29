def add(*args):
    res = 0
    for n in args:
        res += n
    return(res)

""" print(add(3,5,6,22,12)) """


def calculate(n,**kwargs):
    if kwargs.get("add"):
        n += kwargs.get("add")
    n *= kwargs["multiply"]
    print(n)
calculate(2, multiply=5)

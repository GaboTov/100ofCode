from encrypt import encrypt

def test1 ():
    text = 'hello'
    shift = 3
    cri = 'encode'
    expected_output = 'khoor'
    if encrypt(text, shift, cri) == f"You {cri} message is: {expected_output}":
        print('test 1 passed')
    else:
        print('test 1 not passed') 
def test2 ():
    text = '!@#$%^&*()_+'
    shift = 3
    cri = 'encode'
    expected_output = '!@#$%^&*()_+'
    if encrypt(text, shift, cri) == f"You {cri} message is: {expected_output}":
        print('test 2 passed')
    else:
        print('test 1 not passed') 

test1()
test2()
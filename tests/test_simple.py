
from petrocks import Rock

def test_stuff():
    print('in a test')
    assert True

def test_rock_print_info():
    r = Rock('Dave','pointy')
    r.printinfo()
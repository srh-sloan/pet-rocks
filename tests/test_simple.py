
from petrocks import rock

def test_stuff():
    print('in a test')
    assert True

def test_rock_print_info():
    r = rock.Rock('Dave','pointy')
    r.printinfo()
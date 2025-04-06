from calculator import square

def test_positive():
    assert square(2) ==4
    assert square(3) ==9

def test_negative():
    assert square(-2) ==4
    assert square(-3) ==9

def test_zero():
    assert square(0) ==0


"""
testing functions name start with 'test'
pip install pytest
run pytest filename.py

"""
from greeting import greet

def test_greet_fname_lname():
    assert greet('Ajay', 'Singala')

def test_greet_fname():
    assert greet('Ajay')


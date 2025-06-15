import pytest
from calculateFunction import calculate1,calculate2,calculate3,format_product_code,format_product_code1,format_product_code2
# test de version naive
def test_addition():
    assert calculate1(10, 5, '+') == 15

def test_division_arrondie():
    assert calculate1(10, 3, '/') == 3.33  # Division arrondie à deux décimales

def test_division_par_zero():
    assert calculate1(5, 0, '/') == "Erreur : division par zéro"

def test_operateur_invalide():
    assert calculate1(4, 2, '^') == "Erreur : opérateur non valide"
# version de promp professionell

def test_addition():
    assert calculate2(5, 7, '+') == 12

def test_division_arrondie():
    assert calculate2(10, 3, '/') == 3.33  # Résultat arrondi à deux décimales

def test_division_par_zero():
    with pytest.raises(ZeroDivisionError):
        calculate2(4, 0, '/')

def test_operateur_invalide():
    with pytest.raises(ValueError):
        calculate2(8, 2, '%')
# version du promp personna 

def test_addition():
    assert calculate3(10, 5, '+') == 15

def test_soustraction():
    assert calculate3(20, 7, '-') == 13

def test_multiplication():
    assert calculate3(4, 6, '*') == 24

def test_division_arrondie():
    assert calculate3(10, 3, '/') == 3.33

def test_division_par_zero():
    with pytest.raises(ZeroDivisionError):
        calculate3(5, 0, '/')

def test_operateur_invalide():
    with pytest.raises(ValueError):
        calculate3(5, 5, '%')
# zéro shot prompting 

def test_format_valide():
    assert format_product_code("ABC1234XYZ") == "ABC-1234-XYZ"

def test_longueur_invalide():
    with pytest.raises(ValueError, match="exactement 10 caractères"):
        format_product_code("AB123")

def test_caracteres_non_alphanumeriques():
    with pytest.raises(ValueError, match="alphanumérique"):
        format_product_code("ABC1234*YZ")

def test_type_invalide():
    with pytest.raises(ValueError, match="chaîne de caractères"):
        format_product_code(1234567890)  # Non string

def test_format_valide():
    assert format_product_code1("ABC123DEF4") == "ABC-123-DEF4"

def test_longueur_invalide():
    with pytest.raises(ValueError, match="exactement 10 caractères"):
        format_product_code1("AB123")

def test_caracteres_non_alphanumeriques():
    with pytest.raises(ValueError, match="strictement alphanumérique"):
        format_product_code1("ABC12*DEF4")

def test_type_invalide():
    with pytest.raises(ValueError, match="chaîne de caractères"):
        format_product_code1(1234567890)  # Entrée non string


def test_format_abc():
    assert format_product_code2("ABC123DEF4") == "ABC-123-DEF4"

def test_format_xyz():
    assert format_product_code2("XYZ987GHIJ") == "XYZ-987-GHIJ"

def test_longueur_invalide():
    with pytest.raises(ValueError, match="exactement 10 caractères"):
        format_product_code2("SHORT")

def test_caracteres_non_alphanumeriques():
    with pytest.raises(ValueError, match="strictement alphanumérique"):
        format_product_code2("AB@123DEF4")

def test_type_non_string():
    with pytest.raises(ValueError, match="chaîne de caractères"):
        format_product_code2(1234567890)

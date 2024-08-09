from pokedex.pokedex import pokedex
import pytest


def test_good_charizard():
    assert pokedex("charizard") == 200


def test_good_celebi():
    assert pokedex("celebi") == 200


def test_good_landorus():
    assert pokedex("arceus") == 200


def test_good_tepig():
    assert pokedex("tepig") == 200


def test_good_with_debug():
    assert pokedex("tepig", True) == 200


def test_wrong_name():
    assert pokedex("aaaaaaaaa") == 404


def test_wrong_type_int():
    with pytest.raises(TypeError):
        pokedex(12)


def test_wrong_type_list():
    with pytest.raises(TypeError):
        pokedex([10, 4, 8])


def test_wrong_type_tuple():
    with pytest.raises(TypeError):
        pokedex((10, 14))

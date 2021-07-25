import pytest
import encript as en


def test_answer():
    encrt=en.encriptar_info("lol")
    assert en.desencriptar_info(encrt) == "b'lol'"
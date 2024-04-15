def dodaj(a, b):
    return a + b
  
import pytest
from main import dodaj

def test_dodaj():
    assert dodaj(2, 3) == 5
    assert dodaj(-1, 1) == 0
    assert dodaj(0, 0) == 0

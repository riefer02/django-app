import pytest

# Connects our tests with our database
pytestmark = pytest.mark.django_db

from ..models import Cheese

def test__str__():
    cheese = Cheese.objects.create(
    name="Stracchino",
    description="Semi-sweet cheese eaten with starches.", firmness=Cheese.Firmness.SOFT,
    )
    assert cheese.__str__() == "Stracchino" 
    assert str(cheese) == "Stracchino"
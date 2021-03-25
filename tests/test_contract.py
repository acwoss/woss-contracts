import pytest


from woss.contracts import Contract


def test_empty_contract():
    """ Para uma classe de contrato vazia, qualquer classe deve ser válida """
    class Duck(metaclass=Contract):
        pass

    class Spam:
        pass

    assert issubclass(Spam, Duck)
    assert isinstance(Spam(), Duck)

    
def test_contract_must_be_abstract():
    """ Classe de contrato deve ser abstrata por definição """
    class Duck(metaclass=Contract):
        pass

    with pytest.raises(TypeError):
        Duck()

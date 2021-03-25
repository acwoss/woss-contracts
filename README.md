# Contracts

Implementação de contratos em Python.

[![Lint and Tests](https://github.com/acwoss/woss-contracts/actions/workflows/app.yml/badge.svg)](https://github.com/acwoss/woss-contracts/actions/workflows/app.yml)
[![Publish on PyPI](https://github.com/acwoss/woss-contracts/actions/workflows/publish.yml/badge.svg)](https://github.com/acwoss/woss-contracts/actions/workflows/publish.yml)
[![codecov](https://codecov.io/gh/acwoss/woss-contracts/branch/main/graph/badge.svg?token=UN1TBDG4T0)](https://codecov.io/gh/acwoss/woss-contracts)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=acwoss_woss-contracts&metric=alert_status)](https://sonarcloud.io/dashboard?id=acwoss_woss-contracts)

## Instalação

Ao utilizar o PIP para gerenciamento de pacotes, basta executar no terminal:

```
$ pip install woss.contracts
``` 

## Exemplo

```python
from woss.contracts import Contract


class Duck(metaclass=Contract):
    def quack(self):
        pass


class Spam:
    def quack(self):
        print('Quack!')


issubclass(Spam, Duck)  # True
isinstance(Spam(), Duck)  # True
```
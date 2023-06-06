# unit_test_python_cs50

Notas de la clase 5 - Unit Tests del curso CS50P (obvio en YouTube)

## Set up enviroment (MacOs and Linux)
Create a venv:
`python3 -m venv .venv`

Install libraries:
`pip install -r requirements.txt`

## ¿Qué son las pruebas unitarias?
Son pruebas o tests, a funciones que hemos creado.

## Archivos y tipos de tests

calculator.py --> Contiene las funciones de cálculo (raíz cuadrada, multiplicación, etc.).
### Tests vanilla

test_calculator.py --> Contienen las funciones de test para las funciones de cálculo de las funciones de calculator.py.


#### Ejecutar prueba
`python3 test_calculator_with_pytest.py`

Output:
[insertar imagen]

### Tests con pytest
test_calcultor_with_pytest.py --> Contienen las funciones de test, esta vez usa

#### Ejecutar prueba
`pytest test_calcultor_with_pytest.py`

Output:
[insertar imagen]

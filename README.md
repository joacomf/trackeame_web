# API de Trackeame [![Build Status](https://travis-ci.org/joacomf/trackeame_web.svg?branch=master)](https://travis-ci.org/joacomf/trackeame_web)


## Instalar dependencias

```bash
    pipenv install
```
## Ejecutar servidor
```bash
    pipenv shell
    export FLASK_APP=server:init
    flask run
```
## Correr tests
```bash
    python -m pytest tests/ 
    # Para correr test con reporte
    python -m pytest tests/ --html=report.html --self-contained-html
`

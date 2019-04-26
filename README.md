# API de Trackeame

## Instalar dependencias

```bash
    pipenv install
```
## Ejecutar servidor
```bash
    pipenv shell
    FLASK_APP=server:init
    flask run
```
## Correr tests
```bash
    python -m pytest tests/ 
    # Para correr test con reporte
    python -m pytest tests/ --html=report.html --self-contained-html
```
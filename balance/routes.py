from flask import render_template
from balance import app



@app.route("/")
def inicio():
    lista_movimientos = [
        {
            "fecha": "2022-01-06",
            "hora": "13:23:34",
            "concepto": "reyes",
            "es_ingreso": False,
            "cantidad": 80
        },
        {
            "fecha": "2022-01-06",
            "hora": "13:23:34",
            "concepto": "reyes",
            "es_ingreso": True,
            "cantidad": 180
        },
        {
            "fecha": "2022-01-06",
            "hora": "13:23:34",
            "concepto": "lolailo",
            "es_ingreso": False,
            "cantidad": 810
        },
    ]
    return render_template("lista_movimientos.html", movimientos = lista_movimientos)
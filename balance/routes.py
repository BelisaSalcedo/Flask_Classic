from balance import app
@app.route ("/")
def inicio():
    return render_template ('lista_movimientos.html')
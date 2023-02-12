from datetime import date,datetime
from registro_ig import app
from flask import render_template,request,redirect,url_for,flash
from registro_ig.models import select_all,insert,update_by,select_ingreso,apiKey
from registro_ig.forms import MovementsForm
import requests




def validateForm(requestForm):
    hoy = date.today().isoformat()
    errores=[]
    if requestForm['date'] > hoy:
        errores.append("fecha invalida: La fecha introducida es a futuro")
    if requestForm['moneda_from'] == "":
        errores.append("moneda_from vacio: Introduce una moneda para el registro")
    if requestForm['cantidad_from'] == "" or float(requestForm['cantidad_from']) == 0.0:
        errores.append("cantidad vacio o cero: Introduce una cantidad positiva o negativa")   
    return errores
    
@app.route("/")
def index():

    registros = select_all()

    mov = [
    {"ID":1,"date":"02-02-2023","moneda_from":"euro","cantidad_from":"3500","moneda_to":"btc","cantidad_to":"2.0"},
    {"ID":2,"date":"20-01-2023","moneda_from":"euro","cantidad_from":"2000","moneda_to":"btc","cantidad_to":"1.0"},
    {"ID":3,"date":"02-01-2023","moneda_from":"dolar","cantidad_from":"1000","moneda_to":"eth","cantidad_to":"3.0"},
    {"ID":4,"date":"15-01-2023","moneda_from":"dolar","cantidad_from":"5000","moneda_to":"btc","cantidad_to":"2.0"}
    ]
    
    return render_template("index.html",pageTitle="Todos",dataForm=registros)

# @app.route("/compra", methods= ["GET", "POST"])
# def add_sales():

#     euros = float('1000')
#     if euros is None:
#         return "Por favor proporcione una cantidad en euros a convertir"
#     # Realizar la petición a la API CoinAPI para obtener el precio actual de BTC
#     response = requests.get(f'https://rest.coinapi.io/v1/exchangerate/BTC/EUR?apikey={apiKey}')
#     if response.status_code != 200:
#         return "No se pudo obtener el precio actual de BTC"
#     # Calcular la cantidad de BTC equivalente a la cantidad de euros proporcionada
#     btc_price = response.json()["rate"]
#     btc_amount = float(euros) / btc_price

#     # Renderizar la plantilla con la cantidad de BTC calculada
#     return render_template("compra.html", euros=euros, btc=btc_amount)
    

#     if request.method=="GET":
#         pass

#     else:
#         if 'calcular' in request.form:
#             return "aqui se consulta apicoin"

#         if 'comprar' in request.form:
#             return "aqui guardamos en sqlite"

@app.route("/compra",methods=["GET","POST"])
def compra():

    if request.method == "POST":
        euros = request.form.get["euros"]
        # Aquí puedes realizar cualquier otra acción con la variable "euros"
        return render_template("compra.html", euros=euros)

    form=MovementsForm()
    if request.method== "GET": 
        return render_template("compra.html",dataForm=form)
        
    else:
        errores = validateForm(request.form)

        if form.validate_on_submit():
            insert([ request.form['date'],
                     request.form['moneda_from'],
                     request.form['cantidad_from'],
                     request.form['moneda_to'],
                     request.form['cantidad_to'],
                  ])

            return redirect(url_for('index'))

        else:

            return render_template("compra.html", msgError=errores,dataForm=request.form)

              

@app.route("/tradeo",methods=["GET","POST"])
def create():
    form = MovementsForm()
    if request.method == "GET":
        return render_template("tradeo.html",dataForm=form,pageTitle="Alta")
    else:
        

        if form.validate_on_submit():
            
            insert([ form.date.data.isoformat(),
                     form.moneda_from.data,
                     form.cantidad_from.data,
                     form.moneda_to.data,
                     form.cantidad_to.data])
            
            flash('Movimiento registrado correctamente!!!')
            return redirect(url_for('index'))
        else:
            return render_template("tradeo.html",dataForm=form)

#    antarior sin el WTF-form
#     if request.method == "GET":
#         return render_template("new.html",dataForm={})
#     else:
#         #como recibo los datos del formulario
#         errores = validateForm(request.form)

#         if errores:
#             return render_template("new.html",msgError=errores,dataForm=request.form)
#         else:
#             insert([ request.form['date'],
#                      request.form['concept'],
#                      request.form['quantity']  ])
            
#             return redirect(url_for('index'))



@app.route("/venta",methods=["GET","POST"])
def venta():
    form=MovementsForm()
    if request.method== "GET": 
        return render_template("venta.html",dataForm=form)
        
    else:
        errores = validateForm(request.form)

        if form.validate_on_submit():
            insert([ request.form['date'],
                     request.form['moneda_from'],
                     request.form['cantidad_from'],
                     request.form['moneda_to'],
                     request.form['cantidad_to'],
                  ])

            return redirect(url_for('index'))

        else:

            return render_template("venta.html", msgError=errores,dataForm=request.form)




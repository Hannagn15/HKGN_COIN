# Aplicación Web Movimiento Criptomonedas HKGN_COIN

- Programa hecho en python con el framework Flask, CoinApi, con motor de base de datos SQLite
y tiene tres ventadas, la primera, permite comprar, la segunda tradear entre criptos y la tercera vender.

## Se dee crear el entorno virtual venv 

```
pip install -r requirements.txt
pip install requests

```

## Comando para ejecutar el servidor:
```
flask --app main run
```

## Comando para actualizar el servidor con cambios de codigo en tiempo real

```
flask --app main --debug run
```

## acceder a la URL http://127.0.0.1:5000

Al acceder a la Url, en el inicio esta la pagina con el listado de movimientos que se han ejecutado, esta el menu en donde esta: 

    Total ingresos, Total gastos, Saldo actual:

*Compra: aqui la moneda de compra inciial siempre es EUR, poniendo la cantidad deseada a invertir y un desplegable con 7 opciones de Criptomonedas a comprar y asi calcular la cantidad de criptos que se pueden comprar 

*Tradeo: Permite intercambiar criptomonedas por otras previamente compradas y escoger la moneda que se quiere vender.

*Venta: Permite vender las criptomonedas previamente compradas por moneda FIAT 
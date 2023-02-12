from flask import Flask

app = Flask(__name__,instance_relative_config=True)
app.config.from_object("config")

from registro_ig.routes import *

apiKey = '356A76DB-5D23-4441-A990-79B713A11932'


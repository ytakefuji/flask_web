#!/usr/bin/python3
print('Content-Type: text/plain')
print('')
print('This is  test!')
from flask import Flask
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import numpy as np
import base64
from io import BytesIO

app = Flask(__name__)
@app.route("/")
def main():
 fig=Figure()
 ax=fig.subplots()
 ax.plot(np.arange(10),np.arange(10))
 buf=BytesIO()
 fig.savefig(buf,format='png')
 data = base64.b64encode(buf.getbuffer()).decode("ascii")
 return f"<img src='data:image/png;base64,{data}'/>"

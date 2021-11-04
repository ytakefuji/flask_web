# flask_web
This shows how to use a Python flask library to run a webserver.

In order to use the flask, it should be installed by:

$ pip install flask

And open port (5000).

When activating ufw, don't forget opening ssh port!

$ sudo ufw allow 5000

# to run the flask program (matplt.py)
$ FLASK_APP=matplt flask run --host=w.x.y.z


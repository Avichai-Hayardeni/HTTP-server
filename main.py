from flask import Flask, request, Response, render_template, send_file
app = Flask(__name__)


@app.route("/style.css")
def send_css():
    return send_file("style.css")


@app.route("/")
def welcome_page():
    return render_template('welcome response.html', ip=request.remote_addr)


@app.route("/sum")
def sum():
    if "num1" in request.args and "num2" in request.args:
        num1 = int(request.args.get("num1"))
        num2 = int(request.args.get("num2"))
        return render_template('sum response.html', sum=num1+num2)
    else:
        return Response("idiot", status=418)


@app.route("/myname")
def myname():
    if len(request.args) != 1 or "name" not in request.args:
        return Response("idiot", status=400)
    return render_template('myname response.html', name=request.args.get("name"))


if __name__ == '__main__':
    app.run(host="0.0.0.0")

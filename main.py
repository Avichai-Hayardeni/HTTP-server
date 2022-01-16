from flask import Flask, request, Response, render_template, send_file
app = Flask(__name__)


@app.route("/style.css")
def send_css():
    return send_file("style.css")


@app.route("/")
def welcome_page():
    return render_template("welcome.html", ip=request.remote_addr)


@app.route("/sum")
def sum():
    sum = 0
    keys = request.args.keys()
    for key in keys:
        x = request.args.get(key)
        if x.isdigit():
            sum += int(x)
        else:
            return Response(render_template("idiot.html"), status=400)
    return render_template("sum.html", sum=sum)


@app.route("/average")
def average():
    sum = 0
    keys = request.args.keys()
    for key in keys:
        x = request.args.get(key)
        if x.isdigit():
            sum += int(x)
        else:
            return Response(render_template("idiot.html"), status=400)
    average = round(sum/len(keys), 2)
    return render_template("average.html", average=average)


@app.errorhandler(404)
def page_not_found(error):
    return Response(render_template("404.html"), status=404)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="12345")

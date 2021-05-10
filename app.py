from flask import Flask, render_template, request, make_response, send_file
import datetime

app = Flask(__name__)
app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(days=365)
app.config['SECRET_KEY'] = '9hS47A3gh5oiOEF5cs7B0gQersZLxr4lvdEKuJxZ8ScJaNPVBWDLL09jcB2TcwZxYqRBPng2q8sRB4snPs8flNHsMc1'


@app.route('/')
def main_page():
    return render_template("index.html")


@app.route('/kolobok/genomecheck')
def kolobok_genome_page():
    return render_template("kolobok_genome.html")


@app.route('/kolobok')
def main_kolobok_page():
    return render_template("kolobok_genome.html")

@app.route('/kolobok/simplemarketsort')
def kolobok_simplemarketstore_page():
    return render_template("kolobok_simplemarketsort.html")


@app.route('/static/images/<string:filename>')
def images(filename):
    return send_file(f"static\\images\\{filename}", attachment_filename=filename)


if __name__ == "__main__":
    app.run()

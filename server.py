from flask import Flask, request, render_template
app = Flask(__name__)


@app.route('/')
def index():
    html = open('index.html', 'r').read()
    return html


@app.route('/search/')
def results():
    search_data = request.args.get('search_data', '')
    result = ["http://www.dir.bg", "http://www.abv.bg"]
    return render_template('results.html', links=result)

if __name__ == '__main__':
    #app.run()
    app.run(debug=True)

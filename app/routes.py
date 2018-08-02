# need to import app varibales
from app import app
from flask import render_template  # render html files
from app.tables import show_table
from app.parse import getData
from app.graphs import plotPoints

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/graphs')
def graphs():
    x = [1,2,3,4,5]
    y = [7,8,9,0,2]
    xlabel = 'X'
    ylabel = 'Y'
    title = 'Graph'
    my_graph = plotPoints(x, y, xlabel, ylabel, title)
    return render_template('graphs.html', file=my_graph)

@app.route('/tables')
def tables():
    table = show_table()
    return render_template('tables.html', table = table)

@app.route('/parse')
def parse():
    url = 'http://www.arthurleej.com/e-love.html'
    data = getData(url)
    return render_template('parse.html', data=data)

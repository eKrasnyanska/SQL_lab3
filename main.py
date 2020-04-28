import cx_Oracle
import plotly.graph_objects as go
import chart_studio
import chart_studio.plotly as py
import re
import chart_studio.dashboard_objs as dashboard

def fileId_from_url(url):
    """Return fileId from a url."""
    raw_fileId = re.findall("~[A-z.]+/[0-9]+", url)[0][1: ]
    return raw_fileId.replace('/', ':')

chart_studio.tools.set_credentials_file(username='liza.krasnyaskaya', api_key='hBkq8X3Nk61W5JuVfvQy')

login = 'lab3'
password = 'lab3'
host = '127.0.0.1:1521/xe'

query1 = """
select company, count(film) as quantity_films
from films_review
where income > 10000000
group by company"""

query2 = """
select genre, count(genre) as quantity_genres
from films_review 
group by genre"""

query3 = """
select release_date, count(film) as quantity_films
from films_review
group by release_date
order by release_date
"""

list_query = [query1, query2, query3]


try:
    my_con = cx_Oracle.connect(login, password, host)
    print("Connected")
except cx_Oracle.DatabaseError:
    print("Login error")
    exit(0)

list_x_y = []
for query in list_query:
    temp1 = []
    temp2 = []
    cursor = my_con.cursor()
    cursor.execute(query)
    for row in cursor:
        temp1 += [row[0]]
        temp2 += [row[1]]
    list_x_y += [temp1, temp2]
    cursor.close()
my_con.close()
#print(list_x_y)
trace1 = go.Bar(
    x = list_x_y[2],
    y = list_x_y[3]
)
layout1 = go.Layout(
    title_text = 'Film genres',
    xaxis_title = 'Genres',
    yaxis_title = 'Quantity of films'
)
fig1 = go.Figure(data=trace1, layout=layout1)
#fig1.write_html('genres.html', auto_open=True)
genres_sum = py.plot(fig1, filename='genres_sum')

trace2 = go.Pie(
    labels = list_x_y[0],
    values = list_x_y[1]
)
layout2 = go.Layout(
    title_text = 'Best companies with films income more 10 million $'
)
fig2 = go.Figure(data=trace2, layout=layout2)
#fig2.write_html('best.html', auto_open=True)
best_comp = py.plot(fig2, filename='best_company')

trace3 = go.Scatter(
    x = list_x_y[4],
    y = list_x_y[5]
)
layout3 = go.Layout(
    title_text = 'Production of films by years',
    xaxis_title = 'Years',
    yaxis_title = 'Films released'
)
fig3 = go.Figure(data=[trace3], layout=layout3)
#fig3.write_html('films.html', auto_open=True)
film_quantity = py.plot(fig3, filename='film_quantity')

my_dboard = dashboard.Dashboard()
genres_sum_id = fileId_from_url(genres_sum)
best_comp_id = fileId_from_url(best_comp)
film_quantity_id = fileId_from_url(film_quantity)

box1 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': best_comp_id,
    'title': 'Запит 1: Кількість успішних фільмів, що випустила кожна кінокомпанія'
}
box2 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': genres_sum_id,
    'title': 'Запит 2: Розподілення знятих фільмів по жанрам'
}
box3 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': film_quantity_id,
    'title': 'Запит 3: Динаміка випуску фільмів по роках'
}

my_dboard.insert(box1)
my_dboard.insert(box2, 'below', 1)
my_dboard.insert(box3, 'right', 2)

py.dashboard_ops.upload(my_dboard, 'Lab 3')
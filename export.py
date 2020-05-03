import csv
import cx_Oracle

login = 'lab3'
password = 'lab3'
host = '127.0.0.1:1521/xe'

try:
    my_con = cx_Oracle.connect(login, password, host)
    print("Connected")
except cx_Oracle.DatabaseError:
    print("Login error")
    exit(0)
# -------------------------------------------------------------
query = """
select 
TRIM(company_company_name) as company_company_name,
TRIM(company_c_code) as company_c_code,
TRIM(film_film_name) as film_film_name,
TRIM(film_director) as film_director
from company_film
"""
with open("company_film.csv", "w", encoding="ISO-8859-1", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["company", "country", "film", "director"])
    cursor = my_con.cursor()
    cursor.execute(query)
    for row in cursor:
        writer.writerow(row)
    cursor.close()
# -------------------------------------------------------------
query = """
select 
TRIM(company_name) as company_name,
TRIM(country_c_code) as country_c_code
from company
"""
with open("company.csv", "w", encoding="ISO-8859-1", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["company", "country"])
    cursor = my_con.cursor()
    cursor.execute(query)
    for row in cursor:
        writer.writerow(row)
    cursor.close()
# -------------------------------------------------------------
query = """
select 
TRIM(c_code) as c_code
from country
"""
with open("country.csv", "w", encoding="ISO-8859-1", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["country"])
    cursor = my_con.cursor()
    cursor.execute(query)
    for row in cursor:
        writer.writerow(row)
    cursor.close()
# -------------------------------------------------------------
query = """
select 
TRIM(film_name) as film_name,
TRIM(director) as director,
TO_CHAR(release_date, 'yyyy-mm-dd') as release_date,
TRIM(budget) as budget,
TRIM(income) as income
from film
"""
with open("film.csv", "w", encoding="ISO-8859-1", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["film", "director", "released", "budget", "gross"])
    cursor = my_con.cursor()
    cursor.execute(query)
    for row in cursor:
        writer.writerow(row)
    cursor.close()
# -------------------------------------------------------------
query = """
select 
TRIM(genre_genre_name) as genre_genre_name,
TRIM(film_film_name) as film_film_name,
TRIM(film_director) as film_director
from film_genre
"""
with open("film_genre.csv", "w", encoding="ISO-8859-1", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["genre", "film", "director"])
    cursor = my_con.cursor()
    cursor.execute(query)
    for row in cursor:
        writer.writerow(row)
    cursor.close()
# -------------------------------------------------------------
query = """
select 
TRIM(genre_name) as genre_name
from genre
"""
with open("genre.csv", "w", encoding="ISO-8859-1", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["genre"])
    cursor = my_con.cursor()
    cursor.execute(query)
    for row in cursor:
        writer.writerow(row)
    cursor.close()
#-------------------------------------------------------------
my_con.close()
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

file_name = 'movies.csv'
#-------------------------------------------------------------
# fix date format
def func_str(str_date):
    if len(str_date) == 4:
        str_date += '-01-01'
    elif len(str_date) == 7:
        str_date += '-01'
    return str_date
#-------------------------------------------------------------
# insert into table Genre
cursor = my_con.cursor()
query = "insert into genre(genre_name) values (:genre_name)"
cursor.prepare(query)
genre_data = []
with open(file_name,encoding="ISO-8859-1", newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        next_genre = [row['genre']]
        if next_genre not in genre_data:
            genre_data += [next_genre]
cursor.executemany(None, genre_data)
cursor.close()
#-------------------------------------------------------------
# insert into table Country
cursor = my_con.cursor()
query = "insert into country(c_code) values (:c_code)"
cursor.prepare(query)
country_data = []
with open(file_name,encoding="ISO-8859-1", newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        next_country = [row['country']]
        if next_country not in country_data:
            country_data += [next_country]
cursor.executemany(None, country_data)
cursor.close()
#-------------------------------------------------------------
# insert into table Company
cursor = my_con.cursor()
query = "insert into company(company_name, country_c_code) values (:company_name, :country_c_code)"
cursor.prepare(query)
company_data = []
with open(file_name,encoding="ISO-8859-1", newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        next_company = [row['company'], row['country']]
        if next_company not in company_data:
            company_data += [next_company]
cursor.executemany(None, company_data)
cursor.close()
#-------------------------------------------------------------
# insert into table Film
cursor = my_con.cursor()
query = "insert into film(film_name, director, release_date, budget, income) values (:film_name, :director, TO_DATE(:release_date, 'yyyy-mm-dd'), TO_NUMBER(:budget), TO_NUMBER(:income))"
cursor.prepare(query)
film_data = []
with open(file_name,encoding="ISO-8859-1", newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        next_film = [row['name'], row['director'], func_str(row['released']), row['budget'], row['gross']]
        film_data += [next_film]
cursor.executemany(None, film_data)
cursor.close()
#-------------------------------------------------------------
# insert into table Company_Film
cursor = my_con.cursor()
query = "insert into company_film(company_company_name, company_c_code, film_film_name, film_director) values (:company_company_name, :company_c_code, :film_film_name, :film_director)"
cursor.prepare(query)
c_f_data = []
with open(file_name,encoding="ISO-8859-1", newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        next_cf = [row['company'], row['country'], row['name'], row['director']]
        c_f_data += [next_cf]
cursor.executemany(None, c_f_data)
cursor.close()
#-------------------------------------------------------------
# insert into table Film_Genre
cursor = my_con.cursor()
query = "insert into film_genre(genre_genre_name, film_film_name, film_director) values (:genre_genre_name, :film_film_name, :film_director)"
cursor.prepare(query)
f_g_data = []
with open(file_name,encoding="ISO-8859-1", newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        next_fg = [row['genre'], row['name'], row['director']]
        f_g_data += [next_fg]
cursor.executemany(None, f_g_data)
cursor.close()
#-------------------------------------------------------------
my_con.commit()
my_con.close()
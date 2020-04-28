CREATE OR REPLACE VIEW FILMS_REVIEW AS 
  select c.company_name as company, 
f.film_name as film, 
f.income as income,
g.genre_name as genre,
to_number(to_char(f.release_date, 'YYYY')) as release_date
from company c 
    join company_film cf
    on c.company_name = cf.company_company_name
    join film f 
    on cf.film_film_name = f.film_name
    join film_genre fg
    on f.film_name = fg.film_film_name
    join genre g
    on fg.genre_genre_name = g.genre_name;
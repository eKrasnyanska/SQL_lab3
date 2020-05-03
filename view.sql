CREATE VIEW films_review AS
SELECT
company_film.company_company_name as company,
film.film_name as film,
film.income as income,
film_genre.genre_genre_name as genre,
to_number(to_char(film.release_date, 'YYYY')) as release_date
FROM company_film
    JOIN film 
    ON company_film.film_film_name = film.film_name AND company_film.film_director = film.director
    JOIN film_genre
    ON film.film_name = film_genre.film_film_name AND film.director = film_genre.film_director
;
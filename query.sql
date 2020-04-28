--task 1
select company, count(film) as quantity_films
from films_review
where income > 10000000
group by company;

--task2
select genre, count(genre) as quantity_genres
from films_review 
group by genre;

--task3
select release_date, count(film) as quantity_films
from films_review
group by release_date
order by release_date;
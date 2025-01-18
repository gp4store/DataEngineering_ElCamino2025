-- Write an SQL query to retrieve the names and email addresses of customer
-- who live in the city of 'London'. Use a combination of INNER JOINS.

select customer.first_name, customer.last_name, customer.email, city.city
from customer join city
on customer.customer_id = city.city_id
where city like 'London'

-- Write an SQL query to retrieve the film title, category, and language of each film.

select film.title, category.name, language.name
from film
join film_category on film.film_id = film_category.film_id
join category on film_category.category_id = category.category_id
join language on film.language_id = language.language_id
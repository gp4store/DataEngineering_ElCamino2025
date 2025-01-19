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

-- write an sql query to find the names of
-- actors who have played in a film of the 'Horror' category.

select actor.first_name, actor.last_name, category.name 
from actor 
join film_actor on actor.actor_id = film_actor.actor_id
join film on film_actor.film_id = film.film_id 
join film_category on film.film_id = film_category.film_id
join category on film_category.category_id = category.category_id 
where category.name = 'Horror'

-- Write an SQL query to retrieve the names of customers 
-- who have rented the film titled 'DANCING FEVER'

select customer.first_name, customer.last_name
from customer
where customer.customer_id in (
select rental.customer_id
from rental
join inventory on rental.inventory_id = inventory.inventory_id
join film on inventory.film_id = film.film_id
where film.title = 'Dancing Fever'
)

-- Write an SQL query to categorize films into 'Short', 'Medium', or 'Long', 
-- based on their length (less than 60 minutes, between 60 and 120 minutes, and 
-- greater than 120 minutes respectively).

select film.title, film.length,
case
	when film.length < 60 then 'Short'
	when film.length between 60 and 120 then 'Medium'
	else 'Long'
end
from film

-- Write an SQL query to list the customer names along with a status of 'Premium' 
-- if they have spent over $100, 'Regular' if they have spent between $30 and $100, 
-- and 'Basic' otherwise.

select 
customer.first_name,
customer.last_name,
sum(payment.amount) revenue,
    case
        when sum(payment.amount) > 100 then 'Premium'
        when sum(payment.amount) between 30 and 100 then 'Regular'
        else 'Basic'
    end as tier
from customer
join payment on customer.customer_id = payment.customer_id
group by 
customer.customer_id, customer.first_name, customer.last_name

-- Write an SQL query to find the staff member who has made the most sales

select staff.first_name, staff.last_name, sum(payment.amount) as total
from staff
join payment on staff.staff_id = payment.staff_id 
group by staff.staff_id, staff.first_name, staff.last_name

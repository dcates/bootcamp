Use sakila;

-- 1a. Display the first and last names of all actors from the table actor.
select first_name, last_name from actor;

-- 1b. Display the first and last name of each actor in a single column in upper case letters. Name the column Actor Name.
SELECT CONCAT(first_name, ' ', Last_Name) As 'Actor Name' FROM actor;

-- 2a. You need to find the ID number, first name, and last name of an actor, of whom you know only the first name, "Joe."
-- What is one query would you use to obtain this information?
select actor_id, first_name, last_name from actor where first_name = 'joe';

-- 2b. Find all actors whose last name contain the letters GEN:
select * from actor where last_name like '%gen%';

-- 2c. Find all actors whose last names contain the letters LI. This time, order the rows by last name and first name, in that order:
select * from actor where last_name like '%li%' order by last_name, first_name;

-- 2d. Using IN, display the country_id and country columns of the following countries: Afghanistan, Bangladesh, and China:
select country_id, country from country where country in ('Afghanistan', 'Bangladesh', 'China');

-- 3a. Add a middle_name column to the table actor. Position it between first_name and last_name. Hint: you will need to specify the data type.
ALTER TABLE actor
  ADD middle_name VARCHAR(50) after first_name;

-- 3b. You realize that some of these actors have tremendously long last names. Change the data type of the middle_name column to blobs.
ALTER TABLE actor
  modify COLUMN middle_name blob;
  
-- 3c. Now delete the middle_name column.
ALTER TABLE actor
  DROP COLUMN middle_name;

-- 4a. List the last names of actors, as well as how many actors have that last name.
select last_name as 'Last Names',
count(last_name) as 'Count'
from actor
group by last_name;

-- 4b. List last names of actors and the number of actors who have that last name, but only for names that are shared by at least two actors
select last_name as 'Last Names',
count(last_name) as 'Count'
from actor
group by last_name
HAVING COUNT(last_name) >= 2;

-- 4c. Oh, no! The actor HARPO WILLIAMS was accidentally entered in the actor table as GROUCHO WILLIAMS, the name of Harpo's second cousin's husband's yoga teacher. Write a query to fix the record.
select * from actor where first_name = "GROUCHO" and last_name = "WILLIAMS"; -- used to find the actore id
update actor
set first_name = "HARPO"
where actor_id	= 172;

-- 4d. Perhaps we were too hasty in changing GROUCHO to HARPO. It turns out that GROUCHO was the correct name after all! In a single query, if the first name of the actor is currently HARPO, change it to GROUCHO. Otherwise, change the first name to MUCHO GROUCHO, as that is exactly what the actor will be with the grievous error. BE CAREFUL NOT TO CHANGE THE FIRST NAME OF EVERY ACTOR TO MUCHO GROUCHO, HOWEVER! (Hint: update the record using a unique identifier.)
update actor
set first_name = "GROUCHO"
where actor_id	= 172;

-- 5a. You cannot locate the schema of the address table. Which query would you use to re-create it?
CREATE TABLE address1 (
id INTEGER(11) AUTO_INCREMENT NOT NULL,
PRIMARY KEY (id)
);

-- 6a. Use JOIN to display the first and last names, as well as the address, of each staff member. Use the tables staff and address:
select first_name, last_name, address
from address a
inner join staff s
on (a.address_id = s.address_id);

-- 6b. Use JOIN to display the total amount rung up by each staff member in August of 2005. Use tables staff and payment. 
select first_name, last_name, sum(amount) from payment p
inner join staff s
on (p.staff_id = s.staff_id)
where payment_date > '2005-08-01 00:00:00' and payment_date < '2005-09-1 00:00:00' 
group by last_name;

-- 6c. List each film and the number of actors who are listed for that film. Use tables film_actor and film. Use inner join.
select title as 'Film Title', count(actor_id) as 'Actors in Film' from film_actor fa
inner join film f
on (fa.film_id = f.film_id)
group by actor_id;

-- 6d. How many copies of the film Hunchback Impossible exist in the inventory system?
select * from film where title = 'Hunchback Impossible'  -- using this to find the film id
select count(film_id) as 'Total Inventory' from inventory where film_id = 439

-- 6e. Using the tables payment and customer and the JOIN command, list the total paid by each customer. List the customers alphabetically by last name:
select first_name as 'First Name', last_name as 'Last Name', sum(amount) as 'Total Paid' from customer c
inner join payment p
on (c.customer_id = p.customer_id)
group by last_name
order by last_name;

-- 7a. The music of Queen and Kris Kristofferson have seen an unlikely resurgence. As an unintended consequence, films starting with the letters K and Q have also soared in popularity.
	-- Use subqueries to display the titles of movies starting with the letters K and Q whose language is English. 
select * from language -- to get english id
select title
from film
where title in 
(
select title
from film
where title like 'k%' or title like 'q%' and language_id = 1
);
-- 7b. Use subqueries to display all actors who appear in the film Alone Trip.
select first_name as 'First Name', last_name as "Last Name" from actor
where actor_id in
(
select actor_id from film_actor
where film_id in
(
select film_id from film
where title = 'Alone Trip'
));

-- 7c. You want to run an email marketing campaign in Canada, for which you will need the names and email addresses of all Canadian customers. Use joins to retrieve this information.
select first_name as 'First Name', last_name as 'Last Name', email as 'Email Address', country as 'Country' from ((customer cu
inner join address ad
on (cu.address_id = ad.address_id))
inner join city ci
on (ad.city_id = ci.city_id))
inner join country cn
on (cn.country_id = ci.country_id)
where country = 'canada';

-- 7d. Sales have been lagging among young families, and you wish to target all family movies for a promotion. Identify all movies categorized as famiy films.
select title as Title from (category c
inner join film_category fc
on (c.category_id = fc.category_id))
inner join film f
on (f.film_id = fc.film_id)
where name = 'family';

-- 7e. Display the most frequently rented movies in descending order.
select title as 'Title', count(title) as 'Total Rents' from (rental r
inner join inventory i
on (r.inventory_id = i.inventory_id))
inner join film f
on (f.film_id = i.film_id)
group by title
order by count(title) desc;

-- 7f. Write a query to display how much business, in dollars, each store brought in.
select sum(amount) as 'Total Business', s.store_id as "Store ID"  from ((store s
inner join customer c
on (s.store_id = c.store_id))
inner join rental r
on (c.customer_id = r.customer_id))
inner join payment p
on (p.rental_id = r.rental_id)
group by s.store_id;

-- 7g. Write a query to display for each store its store ID, city, and country.
select store_id as 'Store ID', city as "City", country as "Country"  from ((store s
inner join address a
on (s.address_id = a.address_id))
inner join city c
on (c.city_id = a.city_id))
inner join country co
on (co.country_id = c.country_id);

-- 7h. List the top five genres in gross revenue in descending order. (Hint: you may need to use the following tables: category, film_category, inventory, payment, and rental.)
select name as 'Genre', sum(amount) as 'Gross Revenue'  from (((category c
inner join film_category fc
on (c.category_id = fc.category_id))
inner join inventory i
on (fc.film_id = i.film_id))
inner join rental r
on (i.inventory_id = r.inventory_id)
inner join payment p
on (r.rental_id = p.rental_id))
group by name
order by sum(amount) desc
limit 5;

-- 8a. In your new role as an executive, you would like to have an easy way of viewing the Top five genres by gross revenue.
	-- Use the solution from the problem above to create a view. If you haven't solved 7h, you can substitute another query to create a view.
create view top_5_genres as
select name as 'Genre', sum(amount) as 'Gross Revenue'  from (((category c
inner join film_category fc
on (c.category_id = fc.category_id))
inner join inventory i
on (fc.film_id = i.film_id))
inner join rental r
on (i.inventory_id = r.inventory_id)
inner join payment p
on (r.rental_id = p.rental_id))
group by name
order by sum(amount) desc
limit 5;

-- 8b. How would you display the view that you created in 8a?
select * from top_5_genres

-- 8c. You find that you no longer need the view top_five_genres. Write a query to delete it.
drop view top_5_genres;

use sakila;
#1. What query would you run to get all the customers inside city_id = 312? Your query should return customer first name, last name, email, and address.
#select a.first_name, a.last_name, a.email  from customer as a
#join address as b on a.address_id = b.address_id where b.city_id = 312


#2. What query would you run to get all comedy films? Your query should return film title, description, release year, rating, special features, and genre (category).
#select a.title, a.description, a.release_year, a.rating, a.special_features, d.name, b.category_id from category as d
#left join film_category as b on d.category_id= b.category_id
#left join film as a  on a.film_id = b.film_id 
#where d.name='Comedy'

#3. What query would you run to get all the films joined by actor_id=5? Your query should return the actor id, actor name, film title, description, and release year.
#select a.first_name, a.last_name, a.actor_id, c.description, c.title, c.release_year, c.rating  from actor as a
#join film_actor as b on a.actor_id=b.actor_id
#join film as c on c.film_id = b.film_id
#where a.actor_id = 5


#4. What query would you run to get all the customers in store_id = 1 and inside these cities (1, 42, 312 and 459)? 
#Your query should return customer first name, last name, email, and address.

select cus.first_name, cus.last_name, cus.email, adr.address from address as adr
join customer as cus on adr.address_id =cus.address_id
where cus.store_id=1 and adr.city_id = 1 or adr.city_id = 42 or adr.city_id = 312 or adr.city_id = 459
#join store as b on a.address_id = b.address_id

#join city as d on c.city_id=d.city_id
#where b.store_id=1



#5. What query would you run to get all the films with a "rating = G" and "special feature = behind the scenes", 
#joined by actor_id = 15? Your query should return the film title, description, release year, rating, and special feature. 
#Hint: You may use LIKE function in getting the 'behind the scenes' part.

#select a.title, a.description, a.release_year, a.rating, a.special_features from film as a
#join film_actor as b on a.film_id = b.film_id
#join actor as c on b.actor_id=c.actor_id

#where a.rating = 'G' and special_features like '%behind the scenes%' and b.actor_id=15




#6. What query would you run to get all the actors that joined in the film_id = 369? Your query should return the film_id, title, actor_id, and actor_name.
#select a.film_id, a.title, d.first_name, d.last_name    from film as a
#join film_category as b on a.film_id=b.film_id
#join film_actor as c on c.film_id = b.film_id
#join actor as d on c.actor_id = d.actor_id
#where b.film_id=369

#7. What query would you run to get all drama films with a rental rate of 2.99? 
#Your query should return film title, description, release year, rating, special features, and genre (category).

#select a.title, a.description, a.release_year, a.release_year, a.special_features, c.name from film as a
#join film_category as b on a.film_id =b.film_id
#join category as c on c.category_id=b.category_id
#where a.rental_rate=2.99


#8. What query would you run to get all the action films which are joined by SANDRA KILMER? 
#Your query should return film title, description, release year, rating, special features, genre (category), and actor's first name and last name.
#select a.title, a.description, a.release_year, a.rating, a.special_features, d.first_name, d.last_name from film as a
#join film_category as b on a.film_id = b.film_id
#join category as x on x.category_id=b.category_id
#join film_actor as c on b.film_id=c.film_id
#join actor as d on c.actor_id=d.actor_id
#where d.first_name like '%SANDRA%' and d.last_name like '%KILMER%' and x.name = 'Action'  

use world; 
#SELECT c.language, c.percentage, d.name  FROM languages as c  
#left join countries as d on  c.country_id = d.id
#where  c.language = 'Slovene'
#order by percentage desc

#SELECT d.name , count(c.country_code) as City_Count from cities as c 
#join countries as d on c.country_code=d.code
#group by d.name
#order by city_count desc


#select c.name, c.population from cities as c
#join countries as d on c.country_code=d.code and d.name = 'Mexico'
#where  c.population>500000 and c.country_code = d.code
#order by c.population desc

#What query would you run to get all languages in each country with a
# percentage greater than 89%? 
#Your query should arrange the result by percentage in descending order. (1)
 
#select d.name, c.language, c.percentage from languages as c
#join countries as d on c.country_code = d.code
#where c.percentage > 89 
#group by d.name
#order  by c.percentage 

#5. What query would you run to get all the countries with Surface Area below 501 and Population greater than 100,000? (2)
#select * from countries where surface_area<501 and population>100000

#6. What query would you run to get countries with only Constitutional Monarchy with a 
#capital greater than 200 and a life expectancy greater than 75 years? (1)

#select * from countries where government_form like 'constitutional monarchy%' and capital > 200 and life_expectancy > 75

#What query would you run to get all the cities of Argentina inside the Buenos Aires district and have the population greater than 500, 000?
# The query should return the Country Name, City Name, District and Population. (2)

#select d.name, c.name, c.district, c.population from cities as c
#join countries as d on c.country_code=d.code
#where d.name = 'Argentina' and c.population > 500000 and c.district = 'Buenos Aires'

 #What query would you run to summarize the number of countries in each region? The query should display the name of the region and the number of countries.
 #Also, the query should arrange the result by the number of countries in descending order. (2)
 
 select region, count(name)  as number from countries 
 group by region
 order by number desc
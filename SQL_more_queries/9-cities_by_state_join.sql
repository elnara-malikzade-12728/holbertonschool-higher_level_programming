-- lists all the cities from the database
SELECT cities.id, cities.name, states.name FROM cities JOIN states ON cities.id = states.id;

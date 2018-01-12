-- 1
-- SELECT name, language, percentage 
-- FROM languages JOIN countries ON languages.country_code = countries.code
-- WHERE language = "Slovene"
-- ORDER BY percentage DESC;

-- 2
-- SELECT countries.name, COUNT(cities.name) AS count
-- FROM cities JOIN countries ON cities.country_code = countries.code
-- GROUP BY countries.name
-- ORDER BY count DESC

-- 3
-- SELECT countries.name AS country, cities.name AS city, cities.population
-- FROM cities JOIN countries ON cities.country_code = countries.code
-- WHERE countries.name = "Mexico" AND cities.population > 500000
-- ORDER BY cities.population DESC

-- 4
-- SELECT countries.name, languages.language, languages.percentage
-- FROM languages JOIN countries ON languages.country_code = countries.code
-- WHERE languages.percentage > 89
-- ORDER BY languages.percentage DESC
-- 
-- 5
-- SELECT name, surface_area, population FROM countries
-- WHERE surface_area > 501 AND population > 100000
-- ORDER BY surface_area DESC

-- 6
-- SELECT name, government_form, capital, life_expectancy FROM countries
-- WHERE government_form = "Constitutional Monarchy" AND capital > 200 AND life_expectancy > 75
-- ORDER BY capital DESC

-- 7
-- SELECT countries.name, cities.name, cities.district, cities.population
-- FROM cities JOIN countries ON cities.country_code = countries.code
-- WHERE cities.population > 500000 AND countries.name = "Argentina" AND cities.district = "Buenos Aires"
-- ORDER BY cities.district DESC

-- 8
-- SELECT countries.region AS "Region", COUNT(countries.name) AS Count
-- FROM countries
-- GROUP BY countries.region
-- ORDER BY count DESC
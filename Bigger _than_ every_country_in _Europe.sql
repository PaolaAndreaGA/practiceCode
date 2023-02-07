/*6.
Which countries have a GDP greater than every country in Europe? [Give the name only.] (Some countries may have NULL gdp values)*/

SELECT NAME
FROM WORLD
WHERE GDP > ALL(SELECT GDP
FROM WORLD
WHERE CONTINENT = 'EUROPE' AND GDP IS NOT NULL);

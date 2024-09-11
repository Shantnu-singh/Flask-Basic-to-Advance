SELECT name, age+102 as Current_age , survived FROM `train` WHERE survived = "1";
SELECT name, 10000 as Compession , survived FROM `train`;
SELECT DISTINCT sex survived FROM `train`;
SELECT DISTINCT pclass , sex FROM `train`;
SELECT DISTINCT name , pclass , survived FROM `train` WHERE survived = 1 AND pclass = 3;
SELECT DISTINCT name , age , survived FROM `train` WHERE survived = 1 AND age>30;
SELECT DISTINCT name , age , survived FROM `train` WHERE survived = 1 AND age BETWEEN 12 AND 18;
SELECT name , sex FROM train WHERE sex like "male";
SELECT name , sex FROM train WHERE sex IN ("male" , "female");
SELECT name , sex FROM train WHERE sex NOT IN ("male" , "female");
SELECT name , sex FROM train WHERE name like "a%"OR name like "A%";
SELECT name , sex FROM train WHERE name like "%tom%";
SELECT name , sex FROM train WHERE name like "%tom%";
SELECT name , sex FROM train WHERE name like "a_____";
UPDATE users SET name = "Shantnu";
UPDATE passenger SET age = 23 WHERE country like "India";
UPDATE passenger SET country = "INDIA" and destination = "CP" WHERE country like "ind";
UPDATE passenger SET country = "INDIA" where country LIKE "in%";
DELETE FROM passenger WHERE pass_id = 6;
DELETE FROM passenger WHERE destination LIKE "gu%";
SELECT fare , round(fare) as ROundoff , ceil(fare) as CeilFare , floor(fare) AS FloorCeil FROM `train` WHERE 1;
SELECT UPPER(name) FROM `train` WHERE 1;
SELECT concat(sex, "is the gender with this") FROM `train` WHERE 1;
SELECT name , concat(sex, "is the gender with this" , name) FROM `train` WHERE 1;
SELECT name , concat(sex, "is the gender with this" , age) FROM `train` WHERE 1;
SELECT name , max(fare) FROM `train` WHERE 1;
SELECT name , SUM(fare)FROM `train` WHERE 1;
SELECT AVG(fare)FROM `train` WHERE 1;
SELECT COUNT(name) FROM `train` WHERE 1;
SELECT COUNT(DISTINCT(sex)) FROM `train` WHERE 1;
SELECT name , sex, fare FROM `train` ORDER BY fare DESC;
SELECT name , sex, fare FROM `train` ORDER BY fare DESC LIMIT 5;
SELECT name , sex, fare , pclass FROM `train` ORDER BY pclass, fare DESC;
SELECT name , sex, fare ,count(*) FROM `train` GROUP BY pclass;
SELECT name , sex, fare ,count(*) FROM `train` GROUP BY pclass ORDER BY COUNT(*) DESC;
SELECT survived , sum(fare) as TotalFare FROM `train` GROUP BY survived ORDER by TotalFare DESC LIMIT 2;
SELECT pclass , avg(fare) as AVGfare from train GROUP BY pclass ORDER by AVGfare DESC;
# Write your MySQL query statement below
select name from Customer where referee_id <> 2 or referee_id is null
SELECT star , director , SUM(gross- budget) as Profits from movies GROUP By director,star order by Profits DESC LIMIT 5;
SELECT star , genre , SUM(gross- budget) as Profits from movies GROUP By genre,star order by Profits DESC LIMIT 5;
SELECT star , SUM(gross- budget) as Profits from movies GROUP by star order by Profits DESC;
SELECT star , avg(votes) as finalrating FROM movies GROUP BY star HAVING finalrating > 32000 ORDER by finalrating DESC;
SELECT name , (gross - budget) as Profit,
CASE
    when (gross - budget)>1000000000 THEN "Super Hit"
    when (gross - budget)<1000000000 AND (gross - budget)>25000000 THEN "Hit"
    when (gross - budget)<25000000 AND (gross - budget) > 0 THEN "AVg"
    ELSE "LOSS"
END AS verdict
from movies
ORDER by profit DESC;
SELECT COUNT(*) FROM `membership` cross join groups WHERE 1;
SELECT * FROM `membership` cross join groups WHERE 1;
SELECT * from membership m join users u on m.uid =u.id;
SELECT * from membership m left OUTER JOIN users u on m.uid = u.id;
SELECT * from membership m RIGHT OUTER JOIN users u on m.uid = u.id;
SELECT * from membership m left OUTER JOIN users u on m.uid = u.id
UNION 
SELECT * from membership m RIGHT OUTER JOIN users u on m.uid = u.id;
SELECT name, gname , COUNT(*) as totalGrp from membership m JOIN users u ON m.uid = u.id JOIN  groups g on g.gid = m.gid
GROUP by name;
SELECT u1.name , u2.name FROM users u1 JOIN users u2 on u1.id = u2.emergency_contact;
SELECT * FROM `movies` 
ORDER BY budget LIMIT 10;
# Independed movies 
SELECT * FROM `movies` 
WHERE budget = (SELECT max(budget) from movies);

SELECT * FROM `movies` 
WHERE star LIKE "A%";
SELECT * FROM `movies` 
WHERE star in (SELECT star from movies where star LIKE "A%");

SELECT * from movies where star in (SELECT star from (SELECT star, SUM(gross - budget) as "Profit" FROM movies
GROUP BY star 
ORDER by Profit DESC LIMIT 10) A);

SELECT name , genre , (gross - budget) as "Profits" 
from movies m1
WHERE (gross - budget) = (SELECT MAX(gross - budget) FROM movies m2 WHERE m1.genre = m2.genre);

SELECT name , genre , (gross - budget) as "Profits" 
from movies m1
WHERE (gross - budget) = (SELECT MAX(gross - budget) FROM movies m2 WHERE m1.genre = m2.genre);

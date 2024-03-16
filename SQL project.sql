/*Write a SQL query to count the number of characters except the spaces for each actor. 
Return first 10 actors name length along with their name.*/
SELECT ACTOR_ID,FIRST_NAME,LAST_NAME,LENGTH(CONCAT(First_Name,' ',Last_Name)) AS LENGTH FROM ACTOR WHERE ACTOR_ID BETWEEN '1' AND '10';
/*List all Oscar awardees(Actors who received Oscar award) with their full names and length of their names.*/
SELECT FIRST_NAME,LAST_NAME,AWARDS,LENGTH(CONCAT(First_Name,' ',Last_Name)) AS LENGTH FROM ACTOR_AWARD WHERE AWARDS='OSCAR';
/*Find the actors who have acted in the film ‘Frost Headfilm’.*/
SELECT FIRST_NAME,LAST_NAME,TITLE FROM ACTOR  INNER JOIN FILM ON (FILM_ID) WHERE TITLE='FROST HEAD';
/*Pull all the films acted by the actor ‘Will Wilson’.*/

SELECT A.FIRST_NAME,A.LAST_NAME,F.TITLE FROM ACTOR A,FILM F WHERE A.FIRST_NAME='WILL' AND A.LAST_NAME='WILSON';
/*Pull all the films which were rented and return in the month of May.*/
SELECT TITLE AS FILMS,RENTAL_DATE,RETURN_DATE
FROM FILM,RENTAL 
WHERE RENTAL_DATE BETWEEN '2005-05-01' AND '2005-05-31' AND RETURN_DATE BETWEEN '2005-05-01' AND '2005-05-31';
/*Pull all the films with ‘Comedy’ category*/
SELECT F.TITLE,C.NAME AS CATEGORY FROM FILM F,CATEGORY C WHERE C.NAME='COMEDY';
SELECT TITLE FROM FILM LEFT JOIN CATEGORY USING (LAST_UPDATE);

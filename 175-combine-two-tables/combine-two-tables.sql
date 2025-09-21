# Write your MySQL query statement below
SELECT 
    p.firstName,
    p.lastName,  
    a.city, 
    a.state
FROM 
    Person p
LEFT JOIN (
    SELECT  
        personId, 
        city, 
        state 
    FROM Address
) a ON p.personId = a.personId;

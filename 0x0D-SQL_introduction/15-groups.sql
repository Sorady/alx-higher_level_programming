-- Lists the number of records with the same score in the table hbtn_0c_0.second_table
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY score DESC;

USE mysql;

SELECT
  CONCAT('Grants for ', user, '@', host) AS grants,
  privilege_type
FROM
  user_privileges
WHERE
  user IN ('user_0d_1', 'user_0d_2')
ORDER BY
  user,
  host;

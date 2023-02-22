SELECT
    id,
    {{ name }},
    date
FROM
    db
WHERE
    date > "2022-01-01"
ORDER BY
    {{ name }}
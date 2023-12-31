WITH cases_population AS (
    SELECT
        c.date,
        c.LOCATION,
        c.NEW_CASES,
        POPULATION
    FROM
        Cases c
        JOIN Population p ON p.COUNTRY = c.LOCATION
),
SmoothedCases AS (
    SELECT
        cp.LOCATION,
        cp.date,
        cp.NEW_CASES,
        (
            SUM(cp.NEW_CASES) OVER (
                PARTITION BY cp.LOCATION
                ORDER BY
                    cp.date ROWS BETWEEN 6 PRECEDING
                    AND CURRENT ROW
            ) / 7
        ) AS new_cases_smoothed,
        POPULATION
    FROM
        cases_population cp
),
final as(
    SELECT
        t.date,
        t.COUNTRY,
        ROUND(new_cases_smoothed,5) AS new_cases_smoothed,
        CASE
            WHEN t.NEW_TESTS_SMOOTHED = 0 THEN NULL -- Avoid division by zero
            ELSE ROUND(
                (c.new_cases_smoothed) / NULLIF(t.NEW_TESTS_SMOOTHED, 0),
                5
            )
        END AS test_positivity_rate,
        CASE
            WHEN t.NEW_TESTS_SMOOTHED > 1000 THEN 'High Testing'
            ELSE 'Low Testing'
        END AS testing_volume,
        NTILE(4) OVER (
            PARTITION BY t.COUNTRY
            ORDER BY
                t.NEW_TESTS_SMOOTHED
        ) AS testing_quartile
    FROM
        Testing t
        JOIN SmoothedCases c ON t.COUNTRY = c.LOCATION
        AND t.date = c.date
    WHERE
        t.NEW_TESTS_SMOOTHED IS NOT NULL
        AND c.new_cases_smoothed IS NOT NULL
    ORDER BY
        test_positivity_rate DESC
)
SELECT
    *
FROM
    final
WHERE
    test_positivity_rate is not null AND
    COUNTRY IN (:country_list)
ORDER BY
    COUNTRY,
    date;

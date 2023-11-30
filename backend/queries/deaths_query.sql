WITH cases_population AS

(SELECT c."date", c."LOCATION", c."NEW_DEATHS", "POPULATION" FROM "DMAKWANA"."Cases" c
JOIN "DMAKWANA"."Population" p ON p."COUNTRY" = c."LOCATION"),

SmoothedCases AS (
    SELECT 
        cp."LOCATION",
        cp."date",
        cp."NEW_DEATHS",
        (SUM(cp."NEW_DEATHS") OVER (PARTITION BY cp."LOCATION" ORDER BY cp."date" ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) / 7) AS NEW_DEATHS_smoothed,
        POPULATION
    FROM 
        cases_population cp
),
CasesPerMillion AS (
    SELECT 
        LOCATION,
        "date",
        NEW_DEATHS_smoothed,
        (NEW_DEATHS_smoothed / population) * 10000 AS NEW_DEATHS_smoothed_per_million
    FROM 
        SmoothedCases
),
SELECT * FROM CasesPerMillion;
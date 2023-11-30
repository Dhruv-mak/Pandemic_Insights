WITH VaccinationExcessMortality AS (
    SELECT 
        e."date",
        e."COUNTRY",
        e."CUMULATIVE_ESTIMATED_DAILY_EXCESS_DEATHS_PER_100K",
        v.PEOPLE_VACCINATED,
        LAG(e."CUMULATIVE_ESTIMATED_DAILY_EXCESS_DEATHS_PER_100K", 7) OVER (PARTITION BY e."COUNTRY" ORDER BY e."date") AS lagged_excess_mortality,
        LAG(v.PEOPLE_VACCINATED, 7) OVER (PARTITION BY e."COUNTRY" ORDER BY e."date") AS lagged_vaccination_rate
    FROM 
      "DMAKWANA"."Mortality" e
    INNER JOIN 
        "DMAKWANA"."Vaccination" v ON e."COUNTRY" = v."LOCATION" AND e."date" = v."date"
),
FINAL1 AS(
SELECT 
    "date",
    country,
    CUMULATIVE_ESTIMATED_DAILY_EXCESS_DEATHS_PER_100K,
    PEOPLE_VACCINATED,
    lagged_excess_mortality,
    lagged_vaccination_rate,
    (CUMULATIVE_ESTIMATED_DAILY_EXCESS_DEATHS_PER_100K - lagged_excess_mortality) AS change_in_excess_mortality,
    (PEOPLE_VACCINATED - lagged_vaccination_rate) AS change_in_vaccination_rate
FROM 
    VaccinationExcessMortality)
SELECT "date",
    country,
    CUMULATIVE_ESTIMATED_DAILY_EXCESS_DEATHS_PER_100K,
    PEOPLE_VACCINATED,
    lagged_excess_mortality,
    lagged_vaccination_rate, change_in_excess_mortality,
    (change_in_excess_mortality * change_in_vaccination_rate) AS interaction_term
FROM FINAL1
WHERE 
    lagged_excess_mortality IS NOT NULL AND lagged_vaccination_rate IS NOT NULL;

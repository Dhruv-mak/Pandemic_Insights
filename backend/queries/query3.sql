WITH cases_population AS (
    SELECT
        c."date",
        c."LOCATION",
        c."NEW_DEATHS",
        "POPULATION"
    FROM
        "DMAKWANA"."Cases" c
        JOIN "DMAKWANA"."Population" p ON p."COUNTRY" = c."LOCATION"
        AND p."COUNTRY" IN (:country_list)
),
SmoothedCases AS (
    SELECT
        cp."LOCATION",
        cp."date",
        cp."NEW_DEATHS",
        (
            SUM(cp."NEW_DEATHS") OVER (
                PARTITION BY cp."LOCATION"
                ORDER BY
                    cp."date" ROWS BETWEEN 6 PRECEDING
                    AND CURRENT ROW
            ) / 7
        ) AS NEW_DEATHS_smoothed,
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
final_to_use AS (
    SELECT
        location,
        "date",
        NEW_DEATHS_smoothed_per_million
    FROM
        CasesPerMillion
),
EconomicHealthAnalysis AS (
    SELECT
        c."date",
        c.location,
        c.new_deaths_smoothed_per_million,
        d.gdp_per_capita,
        d.cardiovasc_death_rate,
        d.diabetes_prevalence,
        (
            d.gdp_per_capita * c.new_deaths_smoothed_per_million
        ) AS gdp_death_interaction,
        (
            d.cardiovasc_death_rate * c.new_deaths_smoothed_per_million
        ) AS cardiovasc_death_interaction,
        (
            d.diabetes_prevalence * c.new_deaths_smoothed_per_million
        ) AS diabetes_death_interaction,
        (
            d.hospital_beds_per_thousand * c.new_deaths_smoothed_per_million
        ) AS hospital_beds_death_interaction
    FROM
        final_to_use c
        INNER JOIN "DMAKWANA"."Parameters" d ON c.location = d."COUNTRY"
)
SELECT
    "date",
    location,
    new_deaths_smoothed_per_million,
    gdp_death_interaction,
    cardiovasc_death_interaction,
    diabetes_death_interaction,
    hospital_beds_death_interaction,
    ROW_NUMBER() OVER (
        PARTITION BY location
        ORDER BY
            gdp_death_interaction DESC
    ) AS gdp_rank,
    ROW_NUMBER() OVER (
        PARTITION BY location
        ORDER BY
            cardiovasc_death_interaction DESC
    ) AS cardiovasc_rank,
    ROW_NUMBER() OVER (
        PARTITION BY location
        ORDER BY
            diabetes_death_interaction DESC
    ) AS diabetes_rank,
    ROW_NUMBER() OVER (
        PARTITION BY location
        ORDER BY
            hospital_beds_death_interaction DESC
    ) AS hospital_beds_rank
FROM
    EconomicHealthAnalysis
ORDER BY
    location,
    "date"
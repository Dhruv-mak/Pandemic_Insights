WITH EmissionAnalysis AS (
    SELECT 
        "YEAR",
        country,
        "CO2_EMISSION_COAL",
        "CO2_EMISSION_OIL",
        "CO2_EMISSION_GAS",
        "CO2_EMISSION_CEMENT",
        "CO2_EMISSION_FLARING",
        ("CO2_EMISSION_COAL" + "CO2_EMISSION_OIL" + "CO2_EMISSION_GAS" + 
         "CO2_EMISSION_CEMENT" + "CO2_EMISSION_FLARING") AS total_emission
    FROM 
        "DMAKWANA"."Emissions"
),
EmissionRatios AS (
    SELECT 
        "YEAR",
        country,
        total_emission,
        "CO2_EMISSION_COAL" / NULLIF(total_emission, 0) * 100 AS coal_ratio,
        "CO2_EMISSION_OIL" / NULLIF(total_emission, 0) * 100 AS oil_ratio,
        "CO2_EMISSION_GAS" / NULLIF(total_emission, 0) * 100 AS gas_ratio,
        "CO2_EMISSION_CEMENT" / NULLIF(total_emission, 0) * 100 AS cement_ratio,
        "CO2_EMISSION_FLARING" / NULLIF(total_emission, 0) * 100 AS flaring_ratio
    FROM 
        EmissionAnalysis
    WHERE 
        total_emission > 0
),
YEARlyGlobalTrends AS (
    SELECT 
        "YEAR",
        AVG(coal_ratio) AS global_avg_coal_ratio,
        AVG(oil_ratio) AS global_avg_oil_ratio,
        AVG(gas_ratio) AS global_avg_gas_ratio,
        AVG(cement_ratio) AS global_avg_cement_ratio,
        AVG(flaring_ratio) AS global_avg_flaring_ratio
    FROM 
        EmissionRatios
    GROUP BY 
        "YEAR"
),
YEARlyCountryTrends AS (
    SELECT 
        "YEAR",
        country,
        AVG(coal_ratio) AS country_avg_coal_ratio,
        AVG(oil_ratio) AS country_avg_oil_ratio,
        AVG(gas_ratio) AS country_avg_gas_ratio,
        AVG(cement_ratio) AS country_avg_cement_ratio,
        AVG(flaring_ratio) AS country_avg_flaring_ratio
    FROM 
        EmissionRatios
    GROUP BY 
        "YEAR", country
),
CountryYearOverYEARChange AS (
    SELECT 
        yct."YEAR",
        yct.country,
        yct.country_avg_coal_ratio,
        LAG(yct.country_avg_coal_ratio, 1) OVER (PARTITION BY yct.country ORDER BY yct."YEAR") AS prev_YEAR_country_coal,
        yct.country_avg_oil_ratio,
        LAG(yct.country_avg_oil_ratio, 1) OVER (PARTITION BY yct.country ORDER BY yct."YEAR") AS prev_YEAR_country_oil,
        yct.country_avg_gas_ratio,
        LAG(yct.country_avg_gas_ratio, 1) OVER (PARTITION BY yct.country ORDER BY yct."YEAR") AS prev_YEAR_country_gas,
        yct.country_avg_cement_ratio,
        LAG(yct.country_avg_cement_ratio, 1) OVER (PARTITION BY yct.country ORDER BY yct."YEAR") AS prev_YEAR_country_cement,
        yct.country_avg_flaring_ratio,
        LAG(yct.country_avg_flaring_ratio, 1) OVER (PARTITION BY yct.country ORDER BY yct."YEAR") AS prev_YEAR_country_flaring
    FROM 
        YEARlyCountryTrends yct
),
YEAROverYEARChange AS (
    SELECT 
        ygt."YEAR",
        ygt.global_avg_coal_ratio,
        ygt.global_avg_oil_ratio,
        ygt.global_avg_gas_ratio,
        ygt.global_avg_cement_ratio,
        ygt.global_avg_flaring_ratio,
        LAG(ygt.global_avg_coal_ratio, 1) OVER (ORDER BY ygt."YEAR") AS prev_YEAR_global_coal,
        LAG(ygt.global_avg_oil_ratio, 1) OVER (ORDER BY ygt."YEAR") AS prev_YEAR_global_oil,
        LAG(ygt.global_avg_gas_ratio, 1) OVER (ORDER BY ygt."YEAR") AS prev_YEAR_global_gas,
        LAG(ygt.global_avg_cement_ratio, 1) OVER (ORDER BY ygt."YEAR") AS prev_YEAR_global_cement,
        LAG(ygt.global_avg_flaring_ratio, 1) OVER (ORDER BY ygt."YEAR") AS prev_YEAR_global_flaring
    FROM 
        YEARlyGlobalTrends ygt
),
GlobalAndCountryData AS (
    SELECT 
        y."YEAR",
        'global' AS country,
        y.global_avg_coal_ratio AS avg_coal_ratio,
        LAG(y.global_avg_coal_ratio, 1) OVER (ORDER BY y."YEAR") AS prev_YEAR_avg_coal,
        y.global_avg_oil_ratio AS avg_oil_ratio,
        LAG(y.global_avg_oil_ratio, 1) OVER (ORDER BY y."YEAR") AS prev_YEAR_avg_oil,
        y.global_avg_gas_ratio AS avg_gas_ratio,
        LAG(y.global_avg_gas_ratio, 1) OVER (ORDER BY y."YEAR") AS prev_YEAR_avg_gas,
        y.global_avg_cement_ratio AS avg_cement_ratio,
        LAG(y.global_avg_cement_ratio, 1) OVER (ORDER BY y."YEAR") AS prev_YEAR_avg_cement,
        y.global_avg_flaring_ratio AS avg_flaring_ratio,
        LAG(y.global_avg_flaring_ratio, 1) OVER (ORDER BY y."YEAR") AS prev_YEAR_avg_flaring
    FROM 
        YEAROverYEARChange y

    UNION ALL

    SELECT 
        y."YEAR",
        y.country,
        y.country_avg_coal_ratio AS avg_coal_ratio,
        y.prev_YEAR_country_coal AS prev_YEAR_avg_coal,
        y.country_avg_oil_ratio AS avg_oil_ratio,
        y.prev_YEAR_country_oil AS prev_YEAR_avg_oil,
        y.country_avg_gas_ratio AS avg_gas_ratio,
        y.prev_YEAR_country_gas AS prev_YEAR_avg_gas,
        y.country_avg_cement_ratio AS avg_cement_ratio,
        y.prev_YEAR_country_cement AS prev_YEAR_avg_cement,
        y.country_avg_flaring_ratio AS avg_flaring_ratio,
        y.prev_YEAR_country_flaring AS prev_YEAR_avg_flaring
    FROM 
        CountryYearOverYEARChange y
)
SELECT 
    g."YEAR",
    g.country,
    g.avg_coal_ratio,
    (g.avg_coal_ratio - g.prev_YEAR_avg_coal) / NULLIF(g.prev_YEAR_avg_coal, 0) * 100 AS coal_ratio_change,
    g.avg_oil_ratio,
    (g.avg_oil_ratio - g.prev_YEAR_avg_oil) / NULLIF(g.prev_YEAR_avg_oil, 0) * 100 AS oil_ratio_change,
    g.avg_gas_ratio,
    (g.avg_gas_ratio - g.prev_YEAR_avg_gas) / NULLIF(g.prev_YEAR_avg_gas, 0) * 100 AS gas_ratio_change,
    g.avg_cement_ratio,
    (g.avg_cement_ratio - g.prev_YEAR_avg_cement) / NULLIF(g.prev_YEAR_avg_cement, 0) * 100 AS cement_ratio_change,
    g.avg_flaring_ratio,
    (g.avg_flaring_ratio - g.prev_YEAR_avg_flaring) / NULLIF(g.prev_YEAR_avg_flaring, 0) * 100 AS flaring_ratio_change
FROM 
    GlobalAndCountryData g
    WHERE g.country IN (:country_list)
ORDER BY 
    g.country,g."YEAR"
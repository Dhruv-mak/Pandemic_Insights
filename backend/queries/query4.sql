WITH HDI_Components AS (
    SELECT
        country,
        year,
        le,
        eys,
        mys,
        gnipc,
        -- Calculate the indices for each HDI component
        (le - 20) / (85 - 20) AS life_index,
        (eys - 0) / (18 - 0) AS education_expected_index,
        (mys - 0) / (15 - 0) AS education_mean_index,
        -- Calculate income index using logarithms as per the formula
        CASE 
            WHEN gnipc > 100 THEN (LN(gnipc) - LN(100)) / (LN(75000) - LN(100))
            ELSE 0
        END AS income_index
    FROM 
        HDI
    WHERE country IN (:country_list)
),
HDI_Calculations AS (
    SELECT
        country,
        year,
        life_index,
        education_expected_index,
        education_mean_index,
        income_index,
        -- Calculate the Education Index as the average of expected and mean indices
        (education_expected_index + education_mean_index) / 2 AS education_index
    FROM 
        HDI_Components
)
SELECT
    country,
    year,
    -- Calculate the final HDI as the geometric mean of the three indices
    -- Check for negative values before using POWER
    -- ROUND function is used to truncate to 3 decimal places
    CASE 
        WHEN life_index > 0 AND education_index > 0 AND income_index > 0 THEN 
            ROUND(POWER(life_index * education_index * income_index, 1/3), 3)
        ELSE NULL
    END AS hdi
FROM 
    HDI_Calculations;

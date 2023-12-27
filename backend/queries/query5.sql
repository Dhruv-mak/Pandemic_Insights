-- Step 1: Treat zeros and extreme values
-- Set minimum values for MMR and ABR to avoid zeros in geometric mean calculations

-- Step 2: Aggregate across dimensions within each gender group using geometric means
WITH FemaleIndicators AS (
    SELECT
        country, year,
        -- Add a small number to MMR and ABR to ensure they are not zero
        POWER(((10 / GREATEST(MMR, 0.1)) * (1 / GREATEST(ABR, 0.1))), 1/2) AS Health,
        POWER((prf * sef), 1/2) AS Empowerment,
        lfprf
    FROM Inequality
    WHERE MMR BETWEEN 10 AND 1000 AND ABR > 0.1 -- Ensure ABR is greater than 0.1
    AND country IN (:country_list)
),
MaleIndicators AS (
    SELECT
        country, year,
        POWER((prm * sem), 1/2) AS Empowerment,
        LFPRM
    FROM Inequality
    WHERE country IN (:country_list)
),
FemaleGII AS (
    SELECT
        country, year,
        POWER(Health * Empowerment * GREATEST(lfprf, 0.1), 1/3) AS G_F -- Use GREATEST to avoid zero
    FROM FemaleIndicators
),
MaleGII AS (
    SELECT
        country, year,
        POWER(Empowerment * GREATEST(LFPRM, 0.1), 1/3) AS G_M -- Use GREATEST to avoid zero
    FROM MaleIndicators
),
HarmonicMeans AS (
    SELECT
        F.country, F.year,
        -- Check for zero values and handle division by zero
        CASE
            WHEN G_F = 0 OR G_M = 0 THEN NULL -- Avoid division by zero
            ELSE (((1 / G_F) + (1 / G_M))/2) 
        END AS Harmonic_Mean
    FROM FemaleGII F
    JOIN MaleGII M ON F.country = M.country AND F.year = M.year
),

final as(
select country, year ,((POWER(((10/mmr) * (1/abr)), 1/2)) + 1) AS HealthX,
 ((POWER((prf * sef), 1/2) + POWER((prf * sef), 1/2))/2) AS empX,
 ((lfprf + lfprm)/2) AS lfprX
from Inequality
WHERE country IN (:country_list)),

final1 as ( select country, year, POWER((healthX * empX * lfprX), 1/3) as GFM from final),

final2 as
( SELECT
    final1.country, final1.year,
    -- Check for NULL Harmonic_Mean which indicates division by zero was avoided
    CASE
        WHEN Harmonic_Mean IS NULL THEN NULL
        ELSE ROUND(1 - (Harmonic_Mean/ GFM), 5)
    END AS GII
FROM HarmonicMeans join final1 on final1.country= HarmonicMeans.country and final1.year = HarmonicMeans.year
)

select final2.country, final2.year, GII, le,eys,mys,gnipc,abr,mmr,prf,sef,prm,sem,lfprf,lfprm from final2 join HDI h ON final2.country = h.country AND final2.year = h.year
join Inequality e ON final2.country = e.country AND final2.year = e.year
order by country, year
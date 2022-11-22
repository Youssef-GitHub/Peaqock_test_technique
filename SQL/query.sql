BEGIN
DECLARE @coefficient INT,
DECLARE @date DATE,

SET @coefficient = 2
SET @date = "01-09-2005"

select "IdClient"
FROM "ComptesEspece"
WHERE "IdCompte" IN (
	SELECT "IdCompteEspece", SUM("Montant") AS "SumMontant", *
	FROM "ImputationsEspeces"
	WHERE "Sens" = 0
	AND "Nature" = "F"
	AND SumMontant >= @coefficient * (
						SELECT SUM("montant")
						FROM "ImputationsEspeces"
						WHERE "DateImputation" BETWEEN DATEADD(MONTH, -36, @date) AND @date
					)
	GROUP BY "IdCompteEspece"
)
END
//

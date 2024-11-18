/*
Première partie du test:
Réaliser une requête SQL simple permettant de trouver le chiffre
d'affaires (le montant total des ventes), jour par jour, du 1er janvier
2019 au 31 décembre 2019. Le résultat sera trié sur la date à laquelle
la commande a été passée.

Tables utilisées:
- TRANSACTIONS (date, order_id, client_id, prod_id, prod_price, prod_qty)

Format attendu du résultat:
date    | ventes
--------------------
01/01/2020 | 524240
02/01/2020 | 520918
...

Explication : 

- On calcule le produit du prix unitaire (prod_price) par la quantité (prod_qty) pour obtenir le montant total et on somme les ventes par jour.
- Le GROUP BY date permet d'avoir les résultats jour par jour et le ORDER BY date trie les résultats chronologiquement.
*/

SELECT 
    date,
    SUM(prod_price * prod_qty) AS ventes
FROM 
    TRANSACTIONS
WHERE 
    date BETWEEN '2019-01-01' AND '2019-12-31'
GROUP BY 
    date
ORDER BY 
    date;
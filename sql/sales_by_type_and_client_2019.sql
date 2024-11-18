/*
Seconde partie du test:
Réaliser une requête permettant de déterminer, par client et sur la période
allant du 1er janvier 2019 au 31 décembre 2019, les ventes meuble et déco
réalisées.

Tables utilisées:
- TRANSACTIONS (date, order_id, client_id, prod_id, prod_price, prod_qty)
- PRODUCT_NOMENCLATURE (product_id, product_type, product_name)

Format attendu du résultat:
client_id | ventes_meuble | ventes_deco
----------------------------------------
999       | 50            | 14.24
845       | 400           | 60
...


Explication : 

- On fait une jointure entre TRANSACTIONS et PRODUCT_NOMENCLATURE pour accéder au type de produit
- On utilise un CASE WHEN pour séparer les ventes MEUBLE et DECO dans deux colonnes distinctes
- On effectue un group by / groupement par client (client_id)
- Les résultats sont triés par client_id
- La même logique de calcul (prix × quantité) est appliquée pour chaque type de produit
*/

SELECT 
    t.client_id,
    SUM(CASE 
        WHEN pn.product_type = 'MEUBLE' THEN t.prod_price * t.prod_qty 
        ELSE 0 
    END) AS ventes_meuble,
    SUM(CASE 
        WHEN pn.product_type = 'DECO' THEN t.prod_price * t.prod_qty 
        ELSE 0 
    END) AS ventes_deco
FROM 
    TRANSACTIONS t
    JOIN PRODUCT_NOMENCLATURE pn ON t.prod_id = pn.product_id
WHERE 
    t.date BETWEEN '2019-01-01' AND '2019-12-31'
GROUP BY 
    t.client_id
ORDER BY 
    t.client_id;
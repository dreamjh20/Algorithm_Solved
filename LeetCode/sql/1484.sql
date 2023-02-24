-- 1484. Group Sold Products By The Date
-- https://leetcode.com/problems/group-sold-products-by-the-date

SELECT sell_date
     , COUNT(DISTINCT product) num_sold
    -- product 사전순 정렬
     , GROUP_CONCAT(DISTINCT product ORDER BY product) products
FROM Activities
GROUP BY sell_date
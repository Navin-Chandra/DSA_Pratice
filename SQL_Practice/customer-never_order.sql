-- leetcode 183. Customers Who Never Order

select * from Customers c
left join Orders odr
on c.id = odr.customerId
where odr.customerId IS NULL
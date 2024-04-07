# Write your MySQL query statement below
-- select a1.machine_id, round(avg(a2.timestamp-a1.timestamp), 3) as processing_time 
-- from Activity a1
-- join Activity a2 
-- on a1.machine_id=a2.machine_id and a1.process_id=a2.process_id
-- and a1.activity_type='start' and a2.activity_type='end'
-- group by a1.machine_id

select 
a.machine_id,
round(
      (select avg(a1.timestamp) from Activity a1 where a1.activity_type = 'end' and a1.machine_id = a.machine_id) - 
      (select avg(a1.timestamp) from Activity a1 where a1.activity_type = 'start' and a1.machine_id = a.machine_id)
,3) as processing_time
from Activity a
group by a.machine_id

--  top running time
# Write your MySQL query statement below
select act1.machine_id, round(avg(act2.timestamp-act1.timestamp),3) as processing_time
from Activity  act1 join
Activity  act2 on
act1.process_id=act2.process_id and
act1.machine_id = act2.machine_id and
act1.timestamp<act2.timestamp
group by act1.machine_id;
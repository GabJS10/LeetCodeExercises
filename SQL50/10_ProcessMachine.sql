"
+------------+------------+---------------+-----------+
| machine_id | process_id | activity_type | timestamp |
+------------+------------+---------------+-----------+
| 0          | 0          | start         | 0.712     |
| 0          | 0          | end           | 1.520     |
| 0          | 1          | start         | 3.140     |
| 0          | 1          | end           | 4.120     |
| 1          | 0          | start         | 0.550     |
| 1          | 0          | end           | 1.550     |
| 1          | 1          | start         | 0.430     |
| 1          | 1          | end           | 1.420     |
| 2          | 0          | start         | 4.100     |
| 2          | 0          | end           | 4.512     |
| 2          | 1          | start         | 2.500     |
| 2          | 1          | end           | 5.000     |
+------------+------------+---------------+-----------+

| machine_id | process_id | activity_type | timestamp | machine_id | process_id | activity_type | timestamp |
| ---------- | ---------- | ------------- | --------- | ---------- | ---------- | ------------- | --------- |
| 0          | 0          | start         | 0.712     | 0          | 0          | end           | 1.52      |
| 0          | 1          | start         | 3.14      | 0          | 1          | end           | 4.12      |
| 1          | 0          | start         | 0.55      | 1          | 0          | end           | 1.55      |
| 1          | 1          | start         | 0.43      | 1          | 1          | end           | 1.42      |
| 2          | 0          | start         | 4.1       | 2          | 0          | end           | 4.512     |
| 2          | 1          | start         | 2.5       | 2          | 1          | end           | 5         |

| machine_id | process_id | activity_type | timestamp | machine_id | process_id | activity_type | timestamp | processing_time |
| ---------- | ---------- | ------------- | --------- | ---------- | ---------- | ------------- | --------- | --------------- |
| 0          | 0          | start         | 0.712     | 0          | 0          | end           | 1.52      | 0.808           |
| 0          | 1          | start         | 3.14      | 0          | 1          | end           | 4.12      | 0.98            |
| 1          | 0          | start         | 0.55      | 1          | 0          | end           | 1.55      | 1               |
| 1          | 1          | start         | 0.43      | 1          | 1          | end           | 1.42      | 0.99            |
| 2          | 0          | start         | 4.1       | 2          | 0          | end           | 4.512     | 0.412           |
| 2          | 1          | start         | 2.5       | 2          | 1          | end           | 5         | 2...

| machine_id | process_id | activity_type | timestamp | machine_id | process_id | activity_type | timestamp | processing_time |
| ---------- | ---------- | ------------- | --------- | ---------- | ---------- | ------------- | --------- | --------------- |
| 0          | 0          | start         | 0.712     | 0          | 0          | end           | 1.52      | 0.894           |
| 1          | 0          | start         | 0.55      | 1          | 0          | end           | 1.55      | 0.995           |
| 2          | 0          | start         | 4.1       | 2          | 0          | end           | 4.512     | 1.456   

"

select  Activity.machine_id, ROUND(AVG(ac.timestamp - Activity.timestamp),3) AS processing_time
from Activity
inner join Activity ac 
ON (Activity.machine_id = ac.machine_id) 
and (Activity.process_id = ac.process_id)
and (Activity.activity_type="start" and ac.activity_type='end')
group by Activity.machine_id
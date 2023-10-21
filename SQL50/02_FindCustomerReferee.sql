select Customer.name
from Customer
where Customer.referee_id != 2 OR Customer.referee_id IS NULL
<!--where Customer.referee_id NOT IN (2) or Customer.referee_id is null !>

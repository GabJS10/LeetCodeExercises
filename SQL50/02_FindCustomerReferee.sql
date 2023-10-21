select Customer.name
from Customer
where Customer.referee_id != 2 OR Customer.referee_id IS NULL

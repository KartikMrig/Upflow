copy(select O.name,I."status",I."amountOutstanding", To_char((current_date - "dueDate"),'DDD') delay 
from public.invoices I full outer join public.organizations O on I."organizationId" = O.id 
where O.name = 'Blue Consulting' and I.status in ('DUE','OVERDUE','DISPUTED'))
TO 'C:\Users\Kartik\Downloads\upflow\ar_query.csv' DELIMITER ',' CSV HEADER;




copy(select distinct (U.email)
from public.actions A full outer join public.users U on A."performedByUserId" = U.id
where  U.status in ('JOINED') and A."performedByUserId" is null)
TO 'C:\Users\Kartik\Downloads\upflow\user_query.csv' DELIMITER ',' CSV HEADER;





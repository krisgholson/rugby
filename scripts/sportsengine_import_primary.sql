select first_name                 as "First Name",
       last_name                  as "Last Name",
       email                      as "Email",
       to_char(dob, 'YYYY-MM-DD') as "Date of Birth",
       gender                     as "Gender",
       phone_number               as "Phone",
       address_1                  as "Address 1",
       city                       as "City",
       province                   as "State/Province",
       postal_code                as "Postal Code",
       'US'                       as "Country"
from usar_registration
where club in ('Wando Rugby Football Club', 'Charleston Youth and Junior Rugby');
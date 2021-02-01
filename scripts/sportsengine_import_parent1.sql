select split_part(parent_guardian_name, ' ', 1) as "First Name",
       split_part(parent_guardian_name, ' ', 2) as "Last Name",
       parent_guardian_email                    as "Email",
       '1970-01-01'                             as "Date of Birth",
       'Male'                                   as "Gender",
       parent_guardian_phone_number             as "Phone",
       address_1                                as "Address 1",
       city                                     as "City",
       province                                 as "State/Province",
       postal_code                              as "Postal Code",
       'US'                                     as "Country"
from usar_registration
where club in ('Wando Rugby Football Club', 'Charleston Youth and Junior Rugby')
  and parent_guardian_name != '';
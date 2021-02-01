select first_name,
       last_name,
       email,
       parent_guardian_email,
       second_parent_guardian_email,
       to_char(dob, 'YYYY-MM-DD'),
       gender,
       phone_number,
       address_1,
       city,
       province,
       postal_code,
       club_categories
from usar_registration
where club in ('Wando Rugby Football Club', 'Charleston Youth and Junior Rugby')
  and gender = 'Male'
  and (club_categories like 'Coach%' or  club_categories like 'Youth Player%')
--   and (club_categories like 'High School Player%' or  club_categories like 'Youth Player%')
order by last_name, first_name;
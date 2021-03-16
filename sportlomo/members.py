import csv
import os
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

username = os.environ.get('SPORTLOMO_USERNAME')
password = os.environ.get('SPORTLOMO_PASSWORD')

base_url = "https://usarugby.sportsmanager.ie"
auth = {'username': username, 'password': password}


def main():
    return get_members()


def sl_dt_to_iso(date_string):
    cleaned_date = date_string.replace("'", '')
    return datetime.strptime(cleaned_date, '%Y-%m-%d').isoformat() if cleaned_date else None


def reg_dt_to_iso(date_string):
    return datetime.strptime(date_string, '%d/%m/%Y %H:%M').isoformat()


def get_members():
    members = list()
    with requests.Session() as session:
        session.post(base_url + '/Maint-Login.php', data=auth)
        r = session.get(
            base_url + '/sportlomo/user/membership-management/member-export?_method=POST&FilterForm%5Bprimary_identifier%5D=&FilterForm%5Bfirst_name%5D=&FilterForm%5Blast_name%5D=&FilterForm%5Bgender%5D=&FilterForm%5Bemail_address%5D=&FilterForm%5Bidentifier_type%5D=&FilterForm%5Bfrom_dob%5D%5Bmonth%5D=&FilterForm%5Bfrom_dob%5D%5Bday%5D=&FilterForm%5Bfrom_dob%5D%5Byear%5D=&FilterForm%5Bto_dob%5D%5Bmonth%5D=&FilterForm%5Bto_dob%5D%5Bday%5D=&FilterForm%5Bto_dob%5D%5Byear%5D=&FilterForm%5Bfrom_reg_date%5D%5Bmonth%5D=&FilterForm%5Bfrom_reg_date%5D%5Bday%5D=&FilterForm%5Bfrom_reg_date%5D%5Byear%5D=&FilterForm%5Bto_reg_date%5D%5Bmonth%5D=&FilterForm%5Bto_reg_date%5D%5Bday%5D=&FilterForm%5Bto_reg_date%5D%5Byear%5D=&FilterForm%5Bmember_identifier%5D=&FilterForm%5Bseason_id%5D=188&FilterForm%5Bassoc%5D%5B0%5D%5Bgov_body_id%5D=&FilterForm%5Bmembership_status%5D=50&FilterForm%5Bmembership_type%5D=&FilterForm%5Bmembership_level_id%5D=')
        reader = csv.DictReader(r.text.splitlines(), delimiter=',')
        for row in reader:
            members.append(
                {
                    'union': row['Union'] or None,
                    'club': row['Club'] or None,
                    'member_id': row['Member ID'] or None,
                    'first_name': row['Member First Name'] or None,
                    'last_name': row['Last Name'] or None,
                    'gender': row['Gender'] or None,
                    'status': row['Status'] or None,
                    'registration_date': reg_dt_to_iso(row['Registration Date']) if row['Registration Date'] else None,
                    'address_1': row['Address 1  (Primary)'] or None,
                    'address_2': row['Address 2  (Primary)'] or None,
                    'address_3': row['Address 3  (Primary)'] or None,
                    'city': row['City  (Primary)'] or None,
                    'address_4': row['Address 4  (Primary)'] or None,
                    'state': row['State'] or None,
                    'country': row['Country'] or None,
                    'postal_code': row['Post Code (Primary)'] or None,
                    'email': row['E-mail  (Primary)'].lower() if row['E-mail  (Primary)'] else None,
                    'phone': row['Phone Number'] or None,
                    'emergency_name': row['Emergency Name'] or None,
                    'emergency_phone': row['Emergency Phone Number'] or None,
                    'parent_name': row['Parent/Guardian Name'] or None,
                    'parent_email': row['Parent/Guardian Email'].lower() if row['Parent/Guardian Email'] else None,
                    'parent_phone': row['Parent/Guardian Phone Number'] or None,
                    'parent2_name': row['Second Parent/Guardian Name'] or None,
                    'parent2_email': row['Second Parent/Guardian Email'].lower() if row['Second Parent/Guardian Email'] else None,
                    'parent2_phone': row['Second Parent/Guardian Phone Number'] or None,
                    'school': row['School Name'] or None,
                    'membership_package': row['Membership Package'] or None,
                    'birth_date': sl_dt_to_iso(row['Sort DOB']) if row['Sort DOB'] else None,
                    'start_date': sl_dt_to_iso(row['Start Date']) if row['Start Date'] else None,
                    'expiry_date': sl_dt_to_iso(row['Expiry Date']) if row['Expiry Date'] else None,
                    'national_number': row['National Number'] or None
                }
            )
    return members


if __name__ == "__main__":
    main()

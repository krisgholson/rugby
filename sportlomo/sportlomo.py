"""Sportlomo module."""
import csv
from datetime import datetime
import os
import requests
from dotenv import load_dotenv

load_dotenv()

username = os.environ.get('SPORTLOMO_USERNAME')
password = os.environ.get('SPORTLOMO_PASSWORD')

BASE_URL = "https://usarugby.sportsmanager.ie"
PATH_PARAMS = (
    '/sportlomo/user/membership-management/member-export'
    '?_method=POST&FilterForm%5Bmember_id%5D=&FilterForm%5Bfirst_name%5D=&FilterForm%5Blast_name'
    '%5D=&FilterForm%5Bgender%5D=&FilterForm%5Bemail_address%5D=&FilterForm%5Bidentifier_type'
    '%5D=&FilterForm%5Bfrom_dob%5D%5Bmonth%5D=&FilterForm%5Bfrom_dob%5D%5Bday%5D=&FilterForm'
    '%5Bfrom_dob%5D%5Byear%5D=&FilterForm%5Bto_dob%5D%5Bmonth%5D=&FilterForm%5Bto_dob%5D%5Bday'
    '%5D=&FilterForm%5Bto_dob%5D%5Byear%5D=&FilterForm%5Bfrom_reg_date%5D%5Bmonth%5D=&FilterForm'
    '%5Bfrom_reg_date%5D%5Bday%5D=&FilterForm%5Bfrom_reg_date%5D%5Byear%5D=&FilterForm'
    '%5Bto_reg_date%5D%5Bmonth%5D=&FilterForm%5Bto_reg_date%5D%5Bday%5D=&FilterForm%5Bto_reg_date'
    '%5D%5Byear%5D=&FilterForm%5Bmember_identifier%5D=&FilterForm%5Bseason_id%5D=192&FilterForm'
    '%5Bassoc%5D%5B0%5D%5Bgov_body_id%5D=&FilterForm%5Bmembership_status%5D=50&FilterForm'
    '%5Bmembership_type%5D=&FilterForm%5Bmembership_level_id%5D=&FilterForm%5Bgroup_id%5D='
)
AUTH = {'username': username, 'password': password}


def sportlomo_date_to_iso_date(date_string):
    """turn a typical sportlomo date string into an iso formatted date string"""
    if not date_string:
        return None
    cleaned_date = date_string.replace("'", '')
    return datetime.strptime(cleaned_date, '%Y-%m-%d').isoformat() if cleaned_date else None


def registration_date_to_iso_date(date_string):
    """turn a sportlomo registration date string into an iso formatted date string"""
    if not date_string:
        return None
    return datetime.strptime(date_string, '%m/%d/%Y %H:%M').isoformat()


def get_members():
    """make an authenticated request to sportlomo endpoint to return the member export data"""
    members = []
    with requests.Session() as session:
        session.post(BASE_URL + '/Maint-Login.php', data=AUTH)
        response = session.get(BASE_URL + PATH_PARAMS)

        reader = csv.DictReader(response.text.splitlines(), delimiter=',')
        for row in reader:
            members.append(
                {
                    'union': row.get('Union', None),
                    'club': row.get('Club', None),
                    'member_id': row.get('Member ID', None),
                    'first_name': row.get('Member First Name', None),
                    'last_name': row.get('Last Name', None),
                    'gender': row.get('Gender', None),
                    'status': row.get('Status', None),
                    'registration_date': registration_date_to_iso_date(
                        row.get('Registration Date', None)),
                    'address_1': row.get('Address 1  (Primary)', None),
                    'address_2': row.get('Address 2  (Primary)', None),
                    'address_3': row.get('Address 3  (Primary)', None),
                    'city': row.get('City  (Primary)', None),
                    'address_4': row.get('Address 4  (Primary)', None),
                    'state': row.get('State', None),
                    'country': row.get('Country', None),
                    'postal_code': row.get('Post Code (Primary)', None),
                    'email': row.get('E-mail  (Primary)', '').lower(),
                    'phone': row.get('Phone Number', None),
                    'emergency_name': row.get('Emergency Name', None),
                    'emergency_phone': row.get('Emergency Phone Number', None),
                    'parent_name': row.get('Parent/Guardian Name', None),
                    'parent_email': row.get('Parent/Guardian Email', '').lower(),
                    'parent_phone': row.get('Parent/Guardian Phone Number', None),
                    'parent2_name': row.get('Second Parent/Guardian Name', None),
                    'parent2_email': row.get('Second Parent/Guardian Email', '').lower(),
                    'parent2_phone': row.get('Second Parent/Guardian Phone Number', None),
                    'school': row.get('School Name', None),
                    'membership_package': row.get('Membership Package', None),
                    'birth_date': sportlomo_date_to_iso_date(row.get('Sort DOB', None)),
                    'start_date': sportlomo_date_to_iso_date(row.get('Start Date', None)),
                    'expiry_date': sportlomo_date_to_iso_date(row.get('Expiry Date', None)),
                    'national_number': row.get('National Number', None)
                }
            )
    return members

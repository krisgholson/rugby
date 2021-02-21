import csv
import os
import requests
from dotenv import load_dotenv
load_dotenv()

username = os.environ.get('SPORTLOMO_USERNAME')
password = os.environ.get('SPORTLOMO_PASSWORD')

print(username)
print(password)

base_url = "https://usarugby.sportsmanager.ie"
auth = {'username': username, 'password': password}


def main():
    get_members()


def get_members():
    with requests.Session() as session:
        session.post(base_url + '/Maint-Login.php', data=auth)
        r = session.get(
            base_url + '/sportlomo/user/membership-management/member-export?_method=POST&FilterForm%5Bprimary_identifier%5D=&FilterForm%5Bfirst_name%5D=&FilterForm%5Blast_name%5D=&FilterForm%5Bgender%5D=&FilterForm%5Bemail_address%5D=&FilterForm%5Bidentifier_type%5D=&FilterForm%5Bfrom_dob%5D%5Bmonth%5D=&FilterForm%5Bfrom_dob%5D%5Bday%5D=&FilterForm%5Bfrom_dob%5D%5Byear%5D=&FilterForm%5Bto_dob%5D%5Bmonth%5D=&FilterForm%5Bto_dob%5D%5Bday%5D=&FilterForm%5Bto_dob%5D%5Byear%5D=&FilterForm%5Bfrom_reg_date%5D%5Bmonth%5D=&FilterForm%5Bfrom_reg_date%5D%5Bday%5D=&FilterForm%5Bfrom_reg_date%5D%5Byear%5D=&FilterForm%5Bto_reg_date%5D%5Bmonth%5D=&FilterForm%5Bto_reg_date%5D%5Bday%5D=&FilterForm%5Bto_reg_date%5D%5Byear%5D=&FilterForm%5Bmember_identifier%5D=&FilterForm%5Bseason_id%5D=188&FilterForm%5Bassoc%5D%5B0%5D%5Bgov_body_id%5D=&FilterForm%5Bmembership_status%5D=50&FilterForm%5Bmembership_type%5D=&FilterForm%5Bmembership_level_id%5D=')
        print(r.status_code)
        # print(r.text)
        members_file = '/tmp/members.csv'
        with open(members_file, 'w') as out_file:
            out_file.write(r.text)
        with open(members_file, 'r') as in_file:
            reader = csv.DictReader(in_file)
            members = list(reader)
    return members


if __name__ == "__main__":
    main()

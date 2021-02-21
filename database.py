from psycopg2 import connect
import csv
import os
from dotenv import load_dotenv
load_dotenv()

db_name = 'rugby'
db_user = 'postgres'
db_password = os.environ.get('POSTGRES_PASSWORD')
db_host = 'localhost'
table_name = 'usar_registration'

members_file = '/tmp/members.csv'


def main():
    load_db()


def load_db():
    with open(members_file, 'r') as in_file:
        reader = csv.DictReader(in_file)
        members = list(reader)

    try:
        conn = connect(
            dbname=db_name,
            user=db_user,
            host=db_host,
            password=db_password
        )

        cur = conn.cursor()

        insert_statement = """INSERT INTO usar_registration (
        member_id, 
        rugby_union, 
        club,
        first_name,
        last_name,
        gender,
        dob,
        status,
        registration_date,
        address_1,
        address_2,
        city,
        province,
        country,
        postal_code,
        email,
        phone_number,
        emergency_name,
        emergency_phone_number,
        parent_guardian_name,
        parent_guardian_email,
        parent_guardian_phone_number,
        second_parent_guardian_name,
        second_parent_guardian_email,
        second_parent_guardian_phone_number,
        school_name,
        membership_package,
        membership_types,
        club_categories,
        province_categories,
        association_categories,
        sort_dob,
        start_date,
        expiry_date,
        second_member_id) 
        VALUES (
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        TO_DATE(%s, 'DD/MM/YYYY'),
        %s,
        TO_TIMESTAMP(%s, 'DD/MM/YYYY HH24:MI'),
        %s, 
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        TO_DATE(%s, 'YYYY-MM-DD'),
        TO_DATE(%s, 'YYYY-MM-DD'),
        TO_DATE(%s, 'YYYY-MM-DD'),
        %s)"""

        for m in members:
            print(m)
            record_to_insert = (m['Member ID'],
                                m['Union'],
                                m['Club'],
                                m['First Name'],
                                m['Last Name'],
                                m['Gender'],
                                m['DOB'],
                                m['Status'],
                                m['Registration Date'],
                                m['Address 1'],
                                m['Address 2'],
                                m['City'],
                                m['Province'],
                                m['Country'],
                                m['Postal Code'],
                                m['Email'].lower(),
                                m['Phone Number'],
                                m['Emergency Name'],
                                m['Emergency Phone Number'],
                                m['Parent/Guardian Name'].replace('  ', ' '),
                                m['Parent/Guardian Email'].lower(),
                                m['Parent/Guardian Phone Number'],
                                m['Second Parent/Guardian Name'].replace('  ', ' '),
                                m['Second Parent/Guardian Email'].lower(),
                                m['Second Parent/Guardian Phone Number'],
                                m['School Name'],
                                m['Membership Package'],
                                m['Membership Types'],
                                m['Club Categories'],
                                m['Province Categories'],
                                m['Association Categories'],
                                m['Sort DOB'].replace("'", ''),
                                m['Start Date'].replace("'", ''),
                                m['Expiry Date'].replace("'", ''),
                                m['Second Member ID'])
            cur.execute(insert_statement, record_to_insert)

        conn.commit()
        cur.close()

        # print the connection if successful
        print('psycopg2 connection:', conn)

    except Exception as err:
        print('psycopg2 connect() ERROR:', err)
        conn = None

    finally:
        if conn is not None:
            conn.close()


if __name__ == "__main__":
    main()

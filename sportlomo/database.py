import boto3
from members import get_members

dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:4566')
TABLE_NAME = 'rugby_sportlomo_members'


def main():
    reload_member_data()


def reload_member_data():
    recreate_table()
    load_data()


def recreate_table():
    drop_table()
    create_table()


def drop_table():
    table = dynamodb.Table(TABLE_NAME)
    table.delete()
    table.meta.client.get_waiter('table_not_exists').wait(TableName=TABLE_NAME)
    print(TABLE_NAME + ' table deleted.')


def load_data():
    members = get_members()
    table = dynamodb.Table(TABLE_NAME)
    with table.batch_writer(overwrite_by_pkeys=['member_id', 'club']) as batch:
        for m in members:
            batch.put_item(Item=m)


def create_table():
    # Create the DynamoDB table.
    table = dynamodb.create_table(
        TableName=TABLE_NAME,
        KeySchema=[
            {
                'AttributeName': 'member_id',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'club',
                'KeyType': 'RANGE'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'member_id',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'club',
                'AttributeType': 'S'
            }
        ],
        BillingMode='PAY_PER_REQUEST'
    )

    # Wait until the table exists.
    table.meta.client.get_waiter('table_exists').wait(TableName=TABLE_NAME)
    print(TABLE_NAME + ' table created.')


if __name__ == "__main__":
    main()

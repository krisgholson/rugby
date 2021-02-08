import json


def main(event, context):
    print("hello main")


def hello(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response


def registrations(event, context):
    print(event)
    print(context)

    response = {
        "statusCode": 200,
        "body": json.dumps({"yeahh": "baby"})
    }

    return response


if __name__ == "__main__":
    main('', '')

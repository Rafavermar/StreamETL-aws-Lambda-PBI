import json
from extraction.data_extraction import fetch_users_data, extract_identification_data, extract_health_data, \
    extract_employment_data, extract_financial_data, extract_network_data
from powerbi.powerbi_integration import send_to_power_bi
from transformation.data_transformation import transform_user_data
import asyncio


async def process_user(user):
    identification_data = extract_identification_data(user)
    health_data = extract_health_data(user)
    employment_data = extract_employment_data(user)
    financial_data = extract_financial_data(user)
    network_data = extract_network_data(user)

    combined_data = {
        **identification_data,
        **health_data,
        **employment_data,
        **financial_data,
        **network_data
    }

    transformed_data = transform_user_data(combined_data)

    await send_to_power_bi([transformed_data])


async def process_users(users_data):
    for user in users_data:
        await process_user(user)
        await asyncio.sleep(1)


def lambda_handler(event, context):
    loop = asyncio.get_event_loop()
    users_data = loop.run_until_complete(fetch_users_data())
    loop.run_until_complete(process_users(users_data))
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Data processed successfully'})
    }

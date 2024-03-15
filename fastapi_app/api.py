from fastapi import FastAPI
from extraction.data_extraction import fetch_users_data, extract_identification_data, extract_health_data, \
    extract_employment_data, extract_financial_data, extract_network_data
from transformation.data_transformation import transform_user_data
from powerbi.powerbi_integration import send_to_power_bi
import asyncio

app = FastAPI()


@app.post("/process-users")
async def process_users_endpoint():
    users_data = await fetch_users_data()
    for user in users_data:
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
        print("Enviando datos a Power BI:", transformed_data)

        await send_to_power_bi([transformed_data])

        await asyncio.sleep(8)

    return {"message": "Users processed successfully"}

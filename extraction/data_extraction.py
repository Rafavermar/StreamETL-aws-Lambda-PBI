import httpx


async def fetch_users_data():
    url = 'https://dummyjson.com/users'
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()
            return response.json()['users']
    except httpx.HTTPStatusError as e:

        print(f"Error HTTP Response: {e.response.status_code}")
    except httpx.RequestError as e:
        print(f"Request failed to {e.request.url}: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    return []


def extract_identification_data(user):
    return {
        "Id": user["id"],
        "FirstName": user["firstName"],
        "LastName": user["lastName"],
        "MaidenName": user["maidenName"],
        "Username": user["username"],
        "Gender": user["gender"],
        "BirthDate": user["birthDate"],
        "Email": user["email"],
        "Address": user["address"]["address"],
        "City": user["address"]["city"],
        "Coordinates": user["address"]["coordinates"],
        "Postalcode": user["address"]["postalCode"],
        "State": user["address"]["state"]
    }


def extract_health_data(user):
    return {
        "BloodGroup": user["bloodGroup"],
        "Height": user["height"],
        "Weight": user["weight"],
        "EyeColor": user["eyeColor"],
        "HairColor": user["hair"]["color"],
        "HairType": user["hair"]["type"]
    }


def extract_employment_data(user):
    return {
        "companyName": user["company"]["name"],
        "department": user["company"]["department"],
        "title": user["company"]["title"],
        "ein": user["ein"],
        "ssn": user["ssn"]
    }


def extract_financial_data(user):
    return {
        "BankCardNumber": user["bank"]["cardNumber"],
        "cardType": user["bank"]["cardType"],
        "Currency": user["bank"]["currency"],
        "coin": user["crypto"]["coin"],
        "CryptoWallet": user["crypto"]["wallet"],
        "CryptoNetwork": user["crypto"]["network"]
    }


def extract_network_data(user):
    return {
        "Phone": user["phone"],
        "Ip": user["ip"],
        "MacAddress": user["macAddress"],
        "userAgent": user["userAgent"],
        "Domain": user["domain"]
    }

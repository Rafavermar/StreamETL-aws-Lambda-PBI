from datetime import datetime, timezone, timedelta
import random


def transform_user_data(combined_data):
    if 'BirthDate' in combined_data:
        birth_date = datetime.strptime(combined_data['BirthDate'], '%Y-%m-%d')
        age = calculate_age(birth_date)
        combined_data['Age'] = age

    if 'Coordinates' in combined_data and isinstance(combined_data['Coordinates'], dict):
        coordinates = combined_data['Coordinates']
        combined_data['Latitude'] = coordinates.get('lat')
        combined_data['Longitude'] = coordinates.get('lng')
        del combined_data['Coordinates']

    combined_data['CompanyName'] = combined_data.pop('companyName', "")
    combined_data['Department'] = combined_data.pop('department', "")
    combined_data['JobTitle'] = combined_data.pop('title', "")
    combined_data['BankCardType'] = combined_data.pop('cardType', "")
    combined_data['CryptoCoinType'] = combined_data.pop('coin', "")
    combined_data['UserAgentBrowser'] = extract_browser(combined_data.pop("userAgent", ""))

    random_minutes = random.randint(1, 10)
    timestamp = (datetime.now(timezone.utc) + timedelta(minutes=random_minutes)).isoformat(timespec='milliseconds')
    combined_data['Timestamp'] = timestamp

    return combined_data


def calculate_age(born):
    today = datetime.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


def extract_browser(user_agent):
    if 'Chrome' in user_agent:
        return 'Chrome'
    elif 'Firefox' in user_agent:
        return 'Firefox'
    elif 'Safari' in user_agent:
        return 'Safari'
    else:
        return 'Other'

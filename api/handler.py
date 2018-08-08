import json
import requests
import random
import os
from urllib.parse import parse_qs

def whats_for_lunch(event,context):
    params = parse_qs(event['body'])

    if 'text' in params:
        text = params['text'][0]
    else:
        text = ""

    api_response = {"response_type": "in_channel"}
    base_url = "https://developers.zomato.com/api/v2.1/"
    headers = {'Accept': 'application/json', 'user-key': os.environ['ZOMATO_API_KEY']}
    zomato_response = (requests.get(base_url + "search?q=" + str(text) + "&count=" + str("100") + "&entity_id=259&entity_type=city" + "&radius=" + str("0"), headers=headers)).json()

    total = len(zomato_response['restaurants'])
    if total != 0:
        number = random.randint(1,total)
        restaurant = zomato_response['restaurants'][number]['restaurant']
        api_response['text'] = f"{restaurant['name']} - {restaurant['location']['address']}"
        map_url = f"https://www.google.com.au/maps/place/{restaurant['location']['address'].replace(' ', '+')}"
        map_direction = f"https://www.google.com.au/maps/dir/Base2Services,+Australia,+21%2F303+Collins+St,+Melbourne+VIC+3000/{restaurant['location']['address'].replace(' ', '+')}"
        api_response['attachments'] = [
            {
                "actions": [
                    {
                      "type": "button",
                      "text": "website",
                      "url": restaurant['url'],
                      "style": "primary"
                    },
                    {
                      "type": "button",
                      "text": "map",
                      "url": map_url,
                      "style": "primary"
                    },
                    {
                      "type": "button",
                      "text": "directions",
                      "url": map_direction,
                      "style": "primary"
                    }
                ]
            }
        ]


    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Headers": "Content-Type,Authorization,X-Amz-Date,X-Api-Key,X-Amz-Security-Token",
            "Access-Control-Allow-Methods": "DELETE,GET,HEAD,OPTIONS,PATCH,POST,PUT",
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps(api_response)
    }

def coffee_run(event,context):

    api_response = {"response_type": "in_channel"}
    base_url = "https://developers.zomato.com/api/v2.1/"
    headers = {'Accept': 'application/json', 'user-key': os.environ['ZOMATO_API_KEY']}
    zomato_response = (requests.get(base_url + "search?q=" + str("coffee") + "&count=" + str("100") + "&entity_id=259&entity_type=city" + "&radius=" + str("0") + "&cuisine=" + str("cafe"), headers=headers)).json()

    total = len(zomato_response['restaurants'])
    if total != 0:
        number = random.randint(1,total)
        restaurant = zomato_response['restaurants'][number]['restaurant']
        api_response['text'] = f"{restaurant['name']} - {restaurant['location']['address']}"
        map_url = f"https://www.google.com.au/maps/place/{restaurant['location']['address'].replace(' ', '+')}"
        map_direction = f"https://www.google.com.au/maps/dir/Base2Services,+Australia,+21%2F303+Collins+St,+Melbourne+VIC+3000/{restaurant['location']['address'].replace(' ', '+')}"
        api_response['attachments'] = [
            {
                "actions": [
                    {
                      "type": "button",
                      "text": "website",
                      "url": restaurant['url'],
                      "style": "primary"
                    },
                    {
                      "type": "button",
                      "text": "map",
                      "url": map_url,
                      "style": "primary"
                    },
                    {
                      "type": "button",
                      "text": "directions",
                      "url": map_direction,
                      "style": "primary"
                    }
                ]
            }
        ]


    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Headers": "Content-Type,Authorization,X-Amz-Date,X-Api-Key,X-Amz-Security-Token",
            "Access-Control-Allow-Methods": "DELETE,GET,HEAD,OPTIONS,PATCH,POST,PUT",
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps(api_response)
    }

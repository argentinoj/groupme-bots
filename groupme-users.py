"""
groupme-users.py
John Argentino
This script will parse groupme ids using linux commands
"""

import os
import json

"""
result format:
{"response":[<group0>, <group1>, ...]}

group format:
{	"id": <>,
    "group_id": <>,
    "name": <>,
    "phone_number": <>,
    "type": <>,
    "description": <>,
    "image_url": <>,
    "creator_user_id": <>,
    "created_at": <>,
    "updated_at": <>,
    "office_mode": <>,
    "share_url": <>,
    "share_qr_code_url": <>,
    "members": [<member0>, ...],
    "messages": {...},
	"max_members": <>
}

member format:
{
	"user_id": <>,
    "nickname": <>,
    "image_url": <>,
    "id": <>,
    "muted": <>,
    "autokicked": <>,
    "roles": [],
    "name": <>

}

messages format:
{
	"count": <>,
    "last_message_id": <>,
    "last_message_created_at": <>,
    "preview": {
        "nickname": <user who posted the last message>,
        "text": <last message content>,
        "image_url": <url of the image of the user who posted the last one>,
        "attachments": []
    }

}
"""

def get_users():
	token = input("access token:")

	user_cmd = "curl https://api.groupme.com/v3/groups?token=" + token

	result_str = os.popen(user_cmd).read()

	result_dict = json.loads(result_str)

	return result_dict

if __name__ == "__main__":
	res = get_users()
	groups = res["response"]
	for g in groups:
		print(json.dumps(res, indent=4))
		break
"""
groupme-users.py
John Argentino
This script will parse groupme ids using linux commands
"""

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

import os
import json

"""
	get_users
	asks the user for their access token, then returns a list of 
	all the groups associated with the user
"""
def get_groups():
	token = input("access token:")

	user_cmd = "curl https://api.groupme.com/v3/groups?token=" + token

	result_str = os.popen(user_cmd).read()

	result_dict = json.loads(result_str)

	return result_dict['response']

"""
	find_group()
	inputs:
		groups: list of groups each in the dictionary format from the get_groups function
		name: string that is the name of the group we want
	output:
		dictionary of the group if found, None if we did not find the group
"""
def find_group(groups, name):
	try:
		g = list(filter(lambda g: g["name"] == name, groups))
		return g
	except IndexError:
		return None

if __name__ == "__main__":
	groups_list = get_groups()
	#print(groups_list)
	group_name = input("search for a group by name:")
	group = find_group(groups_list, group_name)
	print(json.dumps(group, indent=4))
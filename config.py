import json


def load_config():
    with open("config.json", "r") as file:
        return json.load(file)

config = load_config()

api_id = config["api_id"]
api_hash = config["api_hash"]
group_ids = config["group_ids"]
tracked_usernames = config["tracked_usernames"]
forward_bot_username = config["forward_bot_username"]
enable_forwarding_rule = config["enable_forwarding_rule"]
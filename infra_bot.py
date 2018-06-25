from slackclient import SlackClient
 
slack_client = SlackClient("xoxb-384298611303-386882288433-2qlTlYxbDuYRj1hXMVPeXrok")
 
api_call = slack_client.api_call("users.list")
if api_call.get('ok'):
    users = api_call.get('members')
    for user in users:
        print user.get('name')
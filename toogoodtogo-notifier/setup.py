# Run this file, login from your email and copy down the information that is printed.

from tgtg import TgtgClient
import config

client = TgtgClient(email=config.tgtg["email"])
credentials = client.get_credentials()
print(credentials)
{
    'access_token': '<your_access_token>',
    'refresh_token': '<your_refresh_token>',
    'user_id': '<your_user_id>',
}
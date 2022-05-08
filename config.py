from os import environ as env

from dotenv import load_dotenv

load_dotenv("config.env")

"""
READ EVERYTHING CAREFULLY!!!
"""


DEPLOYING_ON_HEROKU = (
    True  # Make this False if you're not deploying On heroku/Docker
)


if not DEPLOYING_ON_HEROKU:
    BOT_TOKEN = "5373867213:AAFJ-4t7vxd8zmj3weTdx0FWvSnzKrkS0Xg"
    SUDOERS = [1915929975]
    NSFW_LOG_CHANNEL = -1001464756965
    SPAM_LOG_CHANNEL = 1001464756965
    ARQ_API_KEY = "LIMNQJ-CTYXFG-OBCJAC-MWNOIT-ARQ"  # Get it from @ARQRobot
else:
    BOT_TOKEN = env.get("BOT_TOKEN")
    SUDOERS = [int(x) for x in env.get("SUDO_USERS_ID", "").split()]
    NSFW_LOG_CHANNEL = int(env.get("NSFW_LOG_CHANNEL"))
    SPAM_LOG_CHANNEL = int(env.get("SPAM_LOG_CHANNEL"))
    ARQ_API_KEY = env.get("ARQ_API_KEY")

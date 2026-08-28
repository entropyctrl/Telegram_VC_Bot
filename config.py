HEROKU = True  # NOTE Make it false if you're not deploying on heroku.

# NOTE these values are for heroku & Docker.
if HEROKU:
    from os import environ

    from dotenv import load_dotenv

    load_dotenv()  # take environment variables from .env.
    API_ID = int(environ["34565305"])
    API_HASH = environ["934efb3f8005e52b1c36de63c43f40ef"]
    SESSION_STRING = environ[
        "BQIPbLkAWIzvygBpACjg8Sb-8lGJ891lc9xaVWjVWPb_xNYDYo2kjE2z_lRv2P7nHcb0lZFzcnkK__Fd3WpIV4ziLB2j8z4PMPvL07HmmunwyP0-f69sY72wWDf49PGHepwI-8ppUE0J3HN4k05UxLaI8fMV2ibqFxqb5uoYsTRmXGPH_NMfKH8Vyuy3aXPBY5sqQKkn8La__nzN399l4LaZhy009IPrgjvZZJ0bXU3fOCAj5EH0waxrnIB41JNbPaNo15WqOsyvLdoFTZ-Q3ZWuhCqmV7r5pLlXrmxew3mNgWXLJ6H5lzv51gviDVoOQvT6gz-u2RmPhXLFippX8zf6B4dPuQAAAAHnSyeEAA"
    ]  # Check Readme for session
    ARQ_API_KEY = environ["ARQ_API_KEY"]
    CHAT_ID = int(environ["CHAT_ID"])
    DEFAULT_SERVICE = environ.get("DEFAULT_SERVICE") or "youtube"
    BITRATE = int(environ["BITRATE"])

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:
    API_ID = 14371
    API_HASH = "e46b6c854d2bf58a0"
    ARQ_API_KEY = "Get this from @ARQRobot"
    CHAT_ID = -100546355432
    DEFAULT_SERVICE = "saavn"  # Must be one of "youtube"/"saavn"
    BITRATE = 512 # Must be 512/320

# don't make changes below this line
ARQ_API = "https://arq.hamker.in"
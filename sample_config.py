HEROKU = True  # NOTE Make it false if you're not deploying on heroku.

# NOTE these values are for heroku & Docker.
if HEROKU:
    from os import environ

    from dotenv import load_dotenv

    load_dotenv()  # take environment variables from .env.
    API_ID = int(environ["API_ID"])
    API_HASH = environ["API_HASH"]
    SESSION_STRING = environ["SESSION_STRING"]  # Check Readme for session
    ARQ_API_KEY = environ["ARQ_API_KEY"]
    DEFAULT_SERVICE = (
        environ["DEFAULT_SERVICE"]
        if "DEFAULT_SERVICE" in environ
        else "youtube"
    )

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:
    API_ID = 14371
    API_HASH = "e46b6c854d2bf58a0"
    SESSION_STRING = BQBYvLLTZutmbXMpVlyz4NqPBwhwKvyBDcUn20u-6zXcNxi0A1DcM9_LhvGGqZYoipzIwJAwML2Z-WxLISzMrw1rtfmBv7bwPZRQu0KxWs0NAnmddJeXKTuQs12xB3n4XBSKOh0K4NUlxoYmZz94_0GeH3qZTh-_zzy7gybUrHawNq8Xdi_6fhhn9U8m9v-WwBo0GpfpKnIQcK6LPYkYkV3Q0gH10ATHOYIX6FZ5MCJ9-GU5v4ImXvWIVUMMI2AHf4SFyy0YyvDoEtAl-hhN549qFRKP2LF7djPqZhH3FUJMTounBwc6e4lWoq0lEOLQI4qc2CEzKq-WNrsw_42YOKIwSPyBqwA
    ARQ_API_KEY = "Get this from @ARQRobot"
    DEFAULT_SERVICE = "youtube"  # Must be one of "youtube"/"deezer"/"saavn"

# don't make changes below this line
ARQ_API = "https://thearq.tech"

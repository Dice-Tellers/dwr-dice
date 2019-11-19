# Global URLS for extensibility

GATEWAY_URL = "http://127.0.0.1:5000/"

REGISTER_URL = GATEWAY_URL + "users/create"
LOGIN_URL = GATEWAY_URL + "users/login"
LOGOUT_URL = GATEWAY_URL + "users/logout"
USERS_URL = GATEWAY_URL + "users"

READ_URL = GATEWAY_URL + "stories"
SETTINGS_URL = GATEWAY_URL + "stories/new/settings"
ROLL_URL = GATEWAY_URL + "stories/new/roll"
WRITE_URL = GATEWAY_URL + "stories/new/write"
REACTION_URL = GATEWAY_URL + "stories/{}/react"
LATEST_URL = GATEWAY_URL + "stories/latest"
RANGE_URL = GATEWAY_URL + "stories/range"
RANDOM_URL = GATEWAY_URL + "stories/random"

SEARCH_URL = GATEWAY_URL + "search"

# Database in memory
TEST_DB = 'sqlite:///:memory:'

# Default database
DEFAULT_DB = 'sqlite:///dice_service.db'

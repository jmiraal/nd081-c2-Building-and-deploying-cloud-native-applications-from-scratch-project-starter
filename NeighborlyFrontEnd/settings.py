#--------- Flask settings
SERVER_HOST = '0.0.0.0' # Update this for the appropriate front-end website when up
SERVER_PORT = 5000

FLASK_DEBUG = True # Do not use debug mode in prod

# Flask-Restplus settings
SWAGGER_UI_DOC_EXPANSION = 'list'
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False
RESTPLUS_404_HELP = True
API_VERSION = 'v1'
DELETE_CODE_ADD = 'od6LRus1a4wGYh/Ofgnb7EZE6nDsyz1MF9KHAV6x97Z46FadSI4CCQ=='
DELETE_CODE_POST = 'Twq//f2P09s0DDaavNMdUtisaZdPp6l9FnlJYOdP4lkB6acpweTc4A=='

#-------- Azure constants

# API_URL format: "https://[FUNCTION_APP_NAME_GOES_HERE].azurewebsites.net"
API_URL = "https://neighbourlyappjmira.azurewebsites.net/api/"

# for local host if Azure functions served locally
#API_URL = "http://localhost:7071/api"

__author__ = 'kucuny'

__version__ = '0.0.1'

BASE_URL = 'https://api.vultr.com/'

ERROR_CODE = {
    200: "Function successfully executed",
    400: "Invalid API location. Check the URL that you are using",
    403: "Invalid or missing API key. Check that your API key is present and matches your assigned key",
    405: "Invalid HTTP method. Check that the method (POST|GET) matches what the documentation indicates",
    412: "Request failed. Check the response body for a more detailed description",
    500: "Internal server error. Try again at a later time",
    503: "Rate limit hit. API requests are limited to an average of 1/s. Try your request again later."
}

API_FUNCTION_LIST = {
    "v1": {
        "account": {
            "info": "info"
        },
        "app": {
            "list": "list"
        }
    }
}

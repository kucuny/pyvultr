from constants import BASE_URL, API_FUNCTION_LIST, ERROR_CODE


def get_api_url(api_type, api_action, api_version='v1'):
    try:
        url = '/'.join([BASE_URL, api_type, API_FUNCTION_LIST[api_version][api_type][api_action]])
    except IndexError, e:
        url = None

    return url


def get_error_description(error_code):
    if not error_code or type(error_code) is not int:
        return None

    try:
        desc = ERROR_CODE[error_code]
    except IndexError, e:
        desc = None

    return desc

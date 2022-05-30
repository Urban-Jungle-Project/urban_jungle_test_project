from enum import Enum


class ResourcePaths(str, Enum):
    TOKENS = 'tokens'
    USERS = 'users'
    PLANTS = 'plants'


class ResponseCodes(int, Enum):
    SUCCESS = 200
    CREATED = 201
    NO_CONTENT = 204
    UNAUTHORIZED = 401
    BAD_REQUEST = 400


class ErrorMessages(str, Enum):
    REQUIRED_USER_PARAMETERS = 'must include username, email and password fields'
    REQUIRED_USER_PARAMETERS_PASSWORD_RULES = 'Password must be at least 8 characters.'
    REQUIRED_USER_PARAMETERS_USER_RULES = 'Username must be at least 1 character.'
    REQUIRED_USER_PARAMETERS_VALID_EMAIL_ADDRESS = 'Please use a valid email address.'
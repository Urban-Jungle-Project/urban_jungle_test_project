from enum import Enum


class ResourcePaths(str, Enum):
    TOKENS = 'tokens'
    USERS = 'users'
    PLANTS = 'plants'


class ResponseCodes(int, Enum):
    SUCCESS = 200
    NO_CONTENT = 204
    UNAUTHORIZED = 401

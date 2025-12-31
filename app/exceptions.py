class ToolError(Exception):
    """Raised when a tool encounters an error."""

    def __init__(self, message):
        self.message = message


class NewsCatcherError(Exception):
    """Base exception for all NewsCatcher errors"""


class TokenLimitExceeded(NewsCatcherError):
    """Exception raised when the token limit is exceeded"""

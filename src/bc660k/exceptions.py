"""Custom exception types for BC660K operations."""


class BC660KError(RuntimeError):
    """Base error for library-level failures."""


class ATCommandError(BC660KError):
    """Raised when the modem returns ERROR or +CME ERROR for an AT command."""


class ModemTimeoutError(BC660KError):
    """Raised when expected modem response is not received in time."""

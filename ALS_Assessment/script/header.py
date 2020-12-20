"""
Auxuiliary function to print headers
"""

HEADER_STR_FORMAT = "#" * 10 + "\n"

def print_header(header: str) -> None:
    """Prints formatted header."""
    print(
        "\n" * 2,
        HEADER_STR_FORMAT,
        HEADER_STR_FORMAT[0], header.upper(), "\n",
        HEADER_STR_FORMAT
    )

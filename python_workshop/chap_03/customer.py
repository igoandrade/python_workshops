"""
This script displays a user record in the following format: 'John Smith (California)'
"""

def format_customer(first_name, last_name, location=None):
    name = f"{first_name} {last_name}"
    if location:
        return f"{name} ({location})"
    return name

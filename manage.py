#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todoapp.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
# Handle ImportError if Django Is not installed
        

        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # Execute Django management commands from the command line

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    # Call  the main function in this program

    main()

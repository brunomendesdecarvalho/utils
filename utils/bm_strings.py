def is_letter(string):
    if 65 <= ord(string) <= 90 or 97 <= ord(string) <= 122:
        return True
    else:
        return False


def is_upper(string):
    if 65 <= ord(string) <= 90:
        return True
    else:
        return False


def is_lower(string):
    if 97 <= ord(string) <= 122:
        return True
    else:
        return False


def is_number(string):
    if 48 <= ord(string) <= 57:
        return True
    else:
        return False
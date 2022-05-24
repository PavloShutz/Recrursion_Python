def is_palindrome(string: str) -> bool:
    """Return True if the given string is a palindrome"""
    if not isinstance(string, str):
        return False
    string = ''.join(elem for elem in string.lower().split())
    if len(string) < 2:
        return True
    if string[0] != string[-1]:
        return False
    return is_palindrome(string[1:-1])

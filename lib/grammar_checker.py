def grammar_checker(text: str) -> bool:
    if text[0].isupper() and text[-1] in ('.', '!', '?'):
        return True

    return False
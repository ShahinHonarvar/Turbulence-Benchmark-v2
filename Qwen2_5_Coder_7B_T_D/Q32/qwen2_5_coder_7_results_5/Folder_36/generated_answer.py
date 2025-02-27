def insert_after_character(s: str) -> str:
    return ''.join(('HA' if c == 'A' else c for c in s))
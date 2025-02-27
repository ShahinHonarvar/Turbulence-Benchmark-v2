from itertools import zip_longest

def insert_after_character(s: str) -> str:
    s_with_e = ''.join([c + 'e' if c == 'e' else c for c in s])
    return ''.join([a + b for a, b in zip_longest(s, s_with_e, fillvalue='')])
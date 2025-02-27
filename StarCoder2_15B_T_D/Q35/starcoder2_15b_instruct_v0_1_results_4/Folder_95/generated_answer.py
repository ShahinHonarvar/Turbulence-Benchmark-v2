from collections import Counter

def remove_repeat_chars(s: str) -> str:
    """
    Removes repeated characters from a string, preserving the order of characters.
    """
    cnt = Counter(s)
    seen = set()
    result = []
    for c in s:
        if cnt[c] > 1 and c not in seen:
            seen.add(c)
            result.append(c)
    return ''.join(result)
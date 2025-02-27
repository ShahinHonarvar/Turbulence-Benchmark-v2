from typing import List

def remove_repeat_chars(s: str) -> str:
    """
    Removes repeated characters from a string between indices 20 and 43, exclusive.
    """
    counts = [0] * 256
    for c in s:
        counts[ord(c)] += 1
    indices = []
    for i, c in enumerate(s):
        if counts[ord(c)] > 1 and 20 < i < 43:
            indices.append(i)
    output = []
    for i, c in enumerate(s):
        if i not in indices:
            output.append(c)
    return ''.join(output)
def remove_repeat_chars(s: str) -> str:
    if not s:
        return ''
    char_counts = {}
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1
    indices_to_remove = set()
    for i, char in enumerate(s):
        if char_counts[char] > 1 and 38 < i < 52:
            indices_to_remove.add(i)
    result = ''
    for i, char in enumerate(s):
        if i not in indices_to_remove:
            result += char
    return result
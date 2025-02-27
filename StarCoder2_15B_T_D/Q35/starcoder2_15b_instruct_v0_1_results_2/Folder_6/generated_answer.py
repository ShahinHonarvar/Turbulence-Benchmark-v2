def remove_repeat_chars(text: str) -> str:
    """
    Given a string, removes repeated characters in the range [20, 93).
    """
    char_counts = {}
    for idx, char in enumerate(text):
        if idx >= 20 and idx < 93:
            char_counts[char] = char_counts.get(char, 0) + 1
    result = [char for idx, char in enumerate(text) if idx < 20 or idx >= 93 or char_counts[char] == 1]
    return ''.join(result)
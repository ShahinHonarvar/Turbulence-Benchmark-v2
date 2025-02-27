def remove_repeat_chars(text):
    """
    Remove repeated characters in a string.

    Args:
        text (str): Input string.

    Returns:
        str: Modified string without repeated characters.
    """
    char_counts = {}
    for char in text[30:200]:
        char_counts[char] = char_counts.get(char, 0) + 1
    unique_chars = [char for char in text[30:200] if char_counts[char] == 1]
    return text[:30] + ''.join(unique_chars) + text[200:]
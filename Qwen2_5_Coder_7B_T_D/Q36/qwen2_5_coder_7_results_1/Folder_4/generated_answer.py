def filter_chars(s):
    char_to_remove = [chr(i) for i in range(ord('7'), ord('g'))]
    filtered_chars = [char for char in s if char not in char_to_remove]
    return ''.join(filtered_chars)
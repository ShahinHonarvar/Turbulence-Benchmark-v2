def remove_repeat_chars(string):
    char_counts = {}
    for char in string:
        char_counts[char] = char_counts.get(char, 0) + 1
    removed_chars = [char for char, count in char_counts.items() if count > 1 and 60 < string.index(char) < 200]
    filtered_string = ''.join([char for char in string if char not in removed_chars])
    return filtered_string
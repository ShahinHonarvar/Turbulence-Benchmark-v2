def remove_repeat_chars(s):
    char_count = {}
    for i in range(38, 81):
        if i < len(s):
            char = s[i]
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    chars_to_remove = {char for char, count in char_count.items() if count > 1}
    result = [char for i, char in enumerate(s) if char not in chars_to_remove or i <= 38 or i >= 81]
    return ''.join(result)
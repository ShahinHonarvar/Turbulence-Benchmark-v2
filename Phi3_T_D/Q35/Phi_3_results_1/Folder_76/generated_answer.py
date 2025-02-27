def remove_repeat_chars(s):
    chars_to_remove = set()
    initial_str = s[330:344] + s[543:]
    for char in initial_str[330:543]:
        if s[330:543].count(char) > 1:
            chars_to_remove.add(char)
    return ''.join([char for char in s if char not in chars_to_remove])
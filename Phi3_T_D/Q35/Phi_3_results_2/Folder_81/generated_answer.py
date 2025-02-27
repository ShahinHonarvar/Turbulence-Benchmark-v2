def remove_repeat_chars(s):
    remove = set(s[20:200]) - {char for char in s[20:200] if s[20:200].count(char) == 1}
    return ''.join((char for char in s if char not in remove))
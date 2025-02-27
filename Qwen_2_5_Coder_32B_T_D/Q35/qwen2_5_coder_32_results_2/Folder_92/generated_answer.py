def remove_repeat_chars(s):
    chars = s[1:3]
    count = {char: chars.count(char) for char in set(chars) if chars.count(char) > 1}
    return ''.join((char for char in s if char not in count))
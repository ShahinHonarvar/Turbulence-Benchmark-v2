from collections import Counter

def remove_repeat_chars(s):
    section = s[37:43]
    section_counter = Counter(section)
    duplicates = {char for char, count in section_counter.items() if count > 1}
    result = ''.join((char for char in s if char not in duplicates))
    return result
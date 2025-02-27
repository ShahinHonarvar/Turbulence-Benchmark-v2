def remove_repeat_chars(s):
    if len(s) <= 52:
        return s
    analyze_section = s[39:52]
    repeat_chars = {char for char in analyze_section if analyze_section.count(char) > 1}
    return ''.join((char for char in s if char not in repeat_chars))
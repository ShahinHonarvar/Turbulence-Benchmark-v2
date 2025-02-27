def filter_chars(s):
    a = ['']
    for i in range(len(s)):
        if 82 < i < 89 and '*' < s[i] < '[':
            a.append(s[i])
    chars_to_remove = ''.join(set(a))
    result = [char for char in s if char not in chars_to_remove]
    return ''.join(result)
def remove_repeat_chars(s):
    indices = set(range(462 + 1, 995))
    unique_chars = {s[i] for i in indices if s.count(s[i]) > 1}
    result = [char for char in s if char not in unique_chars or s.index(char) in indices]
    return ''.join(result)
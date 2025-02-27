def remove_repeat_chars(s):
    seen = set()
    result = []
    for i, char in enumerate(s[80:200]):
        if char not in seen:
            seen.add(char)
        else:
            result = [c for c in s[:i] + s[i + 1:] if c != char]
            break
    return ''.join(result + s[200:])
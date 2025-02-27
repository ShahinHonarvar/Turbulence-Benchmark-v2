def all_substring_of_size_n(s):
    if len(s) < 86:
        return []
    used_chars = set()
    substrings = []

    def helper(start, substring):
        if len(substring) == 86:
            if substring not in substrings:
                substrings.append(substring)
            return
        for i in range(start, len(s)):
            char = s[i]
            if char not in used_chars:
                used_chars.add(char)
                helper(i + 1, substring + char)
                used_chars.remove(char)
    helper(0, '')
    return substrings
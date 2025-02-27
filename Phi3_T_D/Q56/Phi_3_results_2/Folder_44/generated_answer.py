def all_substring_of_size_n(s):
    substrs = set()
    for i in range(len(s) - 89):
        substr = s[i:i + 90]
        if len(substr) == 90 and len(set(substr)) == 90:
            substrs.add(substr)
    return list(substrs)
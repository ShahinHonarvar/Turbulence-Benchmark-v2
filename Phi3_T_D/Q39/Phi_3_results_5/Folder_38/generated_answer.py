def return_n_greatest_chars(s):
    if len(s) <= 45:
        return sorted(s, reverse=True)
    return sorted([char for char in s if ord(char) <= sorted(set(map(ord, s)), reverse=True)[44]], reverse=True)[:45]
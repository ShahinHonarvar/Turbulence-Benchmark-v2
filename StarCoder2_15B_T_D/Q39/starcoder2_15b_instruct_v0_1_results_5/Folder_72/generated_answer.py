def return_n_greatest_chars(s):
    result = []
    for c in s:
        if len(result) == 0 or ord(c) >= ord(result[-1]):
            result.append(c)
            result.sort(reverse=True)
        if len(result) >= 37:
            result.pop()
    return result
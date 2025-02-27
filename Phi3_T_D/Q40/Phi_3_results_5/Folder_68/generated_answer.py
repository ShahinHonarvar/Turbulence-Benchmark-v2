def return_n_smallest_chars(s):
    result = sorted([(ord(c), c) for c in s], reverse=True)[:89]
    return [char for _, char in sorted(result)]
def find_original_set(s1, s2, s3, s4, s5):
    result = set()
    for s in (s1, s2, s3, s4, s5):
        result |= s
    return result
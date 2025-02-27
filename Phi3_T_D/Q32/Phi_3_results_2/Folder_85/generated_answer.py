def insert_after_character(s):
    return s.replace('o', 'oa', s.count('o') - 1) + 'a' * s.endswith('o')
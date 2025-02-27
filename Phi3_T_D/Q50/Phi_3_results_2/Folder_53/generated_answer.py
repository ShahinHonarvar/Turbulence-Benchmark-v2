def if_contains_anagrams(lst):

    def count_chars(s):
        return sorted([c.lower() for c in s if c.isalpha()])
    counted = {}
    for word in lst:
        if len(word) >= 3:
            char_list = count_chars(word)
            key = ''.join(char_list)
            if key in counted:
                counted[key] += 1
                if counted[key] >= 2:
                    return True
            else:
                counted[key] = 1
    return False
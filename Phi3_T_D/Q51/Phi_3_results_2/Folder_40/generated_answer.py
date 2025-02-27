def if_contains_anagrams(str_list):

    def get_sorted_string(s):
        return ''.join(sorted(s.lower()))
    count = 0
    seen = dict()
    for word in str_list:
        if len(word) < 3:
            continue
        sorted_word = get_sorted_string(word)
        if sorted_word not in seen:
            seen[sorted_word] = 1
        else:
            count += 1
        if count > 29:
            return False
    return True
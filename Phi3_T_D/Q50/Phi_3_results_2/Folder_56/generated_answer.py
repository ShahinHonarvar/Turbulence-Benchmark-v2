def if_contains_anagrams(string_list):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    count = 0
    checked = set()
    for i in range(len(string_list)):
        if string_list[i] in checked:
            continue
        key = normalize(string_list[i])
        potential_anagrams = [j for j in range(i + 1, len(string_list)) if len(string_list[j]) >= 3 and normalize(string_list[j]) == key]
        count += len(potential_anagrams)
        checked.update(potential_anagrams)
    return count >= 77
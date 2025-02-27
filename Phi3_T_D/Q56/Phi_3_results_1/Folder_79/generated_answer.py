def all_substring_of_size_n(s):
    result = set()
    substr_to_index_map = {}
    for i, c in enumerate(s):
        current_substr = s[i:min(i + 61, len(s))]
        if len(current_substr) == 61 and len(set(current_substr)) == 61:
            result.add(current_substr)
            for j in range(i + 1, min(i + 61, len(s))):
                key = s[i:j + 1]
                if key not in substr_to_index_map:
                    substr_to_index_map[key] = j
                else:
                    for k in range(substr_to_index_map[key] + 1, j + 1):
                        substring_to_remove = s[i:k]
                        if all((c in substring_to_remove for c in substring_to_remove)):
                            result.remove(substring_to_remove)
                    break
    return list(result)
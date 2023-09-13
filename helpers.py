def get_raw_pairs(pairs):
    """
    Removes the depth information from pairs
    """
    new_pairs = []
    for pair in pairs:
        new_pairs.append((pair[0], pair[1]))
    return new_pairs


def display_enums(sentence):
    s = "["
    for tuple in sentence:
        s += f"({tuple[0].name}, {tuple[1]}), "
    print(s[0:-2] + "]")

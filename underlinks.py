from enum import Enum

# class SymbolSet(Enum):
#     VERTICAL = '│'
#     LEFTCORNER = '└'
#     RIGHTCORNER = '┘'
#     HORINZONTAL = '─'


class SymbolSet(Enum):
    VERTICAL = "║"
    LEFTCORNER = "╚"
    RIGHTCORNER = "╝"
    HORINZONTAL = "═"


def draw_underlinks(tuple_sentence, pairs, gap=3):
    formatted_sentence = []
    for tuple in tuple_sentence:
        if tuple[1] < 0:
            formatted_sentence.append(f'{tuple[0].name}_{"l"*-tuple[1]}')
        elif tuple[1] > 0:
            formatted_sentence.append(f'{tuple[0].name}_{"r"*tuple[1]}')
        else:
            formatted_sentence.append(f"{tuple[0].name}")

    middle_indexes = get_middle_str_indexes(formatted_sentence, gap)
    # print((' '*(gap+2)).join([str(x) for x in range(len(formatted_sentence))]))
    print((" " * gap).join(formatted_sentence))

    cur_depth = 1
    max_depth = max(list(map(lambda tuple: tuple[2], pairs)))

    while cur_depth <= max_depth:
        underlink_chars = ["" for _ in range(len(pairs) * 2)]
        for pair in pairs:
            depth = pair[2]
            if depth == cur_depth:
                underlink_chars[pair[0]] = SymbolSet.LEFTCORNER.value
                underlink_chars[pair[1]] = SymbolSet.RIGHTCORNER.value
            elif depth > cur_depth:
                underlink_chars[pair[0]] = SymbolSet.VERTICAL.value
                underlink_chars[pair[1]] = SymbolSet.VERTICAL.value
        cur_char_index = 0
        gap_char = " "
        cur_line = ""
        # This reads underlink_chars and draws the different symbols when
        # on a index that is in the middle of a token or not.
        for i in range(max(middle_indexes) + 1):
            if i in middle_indexes:
                cur_line += underlink_chars[cur_char_index]
                if underlink_chars[cur_char_index] == SymbolSet.LEFTCORNER.value:
                    gap_char = SymbolSet.HORINZONTAL.value
                if underlink_chars[cur_char_index] == SymbolSet.RIGHTCORNER.value:
                    gap_char = " "
                if underlink_chars[cur_char_index] == "":
                    cur_line += gap_char
                cur_char_index += 1
            else:
                cur_line += gap_char
        print(cur_line)
        cur_depth += 1


# returns list with indexes of all the middles of each str


def get_middle_str_indexes(sentence, gap=3):
    total_length = 0
    out = []
    for token in sentence:
        mid = len(token) // 2
        out.append(total_length + mid)
        total_length += gap + len(token)
    return out

from basic import Basic as B
from transitions import transitions
from dictionary import dictionary
from helpers import display_enums, get_raw_pairs
from underlinks import draw_underlinks


def main():
    sentence = input("Enter a sentence: ")
    components = sentence_to_components(sentence)
    display_enums(components)
    valid, pairs = sentence_validity_preprocessing(components)
    print(valid)
    if valid:
        print(sentence)
        draw_underlinks(components, pairs)
        print(get_raw_pairs(pairs))


def sentence_to_components(sentence_string):
    # Each component is stored as a tuple such that (base, precedence)
    components = []
    sentence = sentence_string.split()
    # Get the base for each word in the sentence from the dictionary
    for word in sentence:
        components.extend(dictionary[word])
    return components


def sentence_validity_preprocessing(components):
    # Sentences cannot have an odd number of components
    if len(components) % 2 == 1:
        return False, []
    valid, pairs, _ = sentence_validity(components, 0, len(components) - 1)
    return valid, pairs


def sentence_validity(components, start, end, pairs=[]):
    """
    Recursive method to reduce an entire sentence. Will return True if
    the sentence can be reduced all the way to 1, as well as a list of all
    the pairs made in the reduction. If the reduction is invalid, the pairs
    will be returned as an empty list

    @param sentence: List of components
    @param start: Starting index of subsection
    @param end: End index of subsection
    @param pairs: List of all the pairs that reduce with each other

    @return boolean, list
    """
    # Base case: Empty sentence is valid
    if end - start <= 0:
        return True, pairs, 0
    # Work our way backwards through the sentence, checking every
    # other component, and seeing if we have a valid pair
    for index in range(end - 1, start - 1, -2):
        # Check if the given pair is a valid match
        if match(components[index], components[end]):
            # Recursive call for outer
            valid_outer, pairs, depth_outer = sentence_validity(
                components, start, index - 1, pairs
            )
            # Recursive call for inner
            valid_inner, pairs, depth_inner = sentence_validity(
                components, index + 1, end - 1, pairs
            )
            # Calculate depth of current component
            depth = max(depth_inner, depth_outer - 1) + 1

            # Add our new pair
            pairs.append((index, end, depth))

            return valid_outer and valid_inner, pairs, depth
    # If we check every term and do not find a match, the sentence is invalid
    return False, [], 0


def match(left, right):
    """
    Checks if the left and right tuple can be reduced to 1
    """
    # Check that the left precedence is 1 less that the right precedence
    if left[1] - 1 == right[1]:
        return False
    # Check if the tuples are the same basic type, no further checks needed
    if left[0] == right[0]:
        return True
    # Transitions can only occur on 0 precedence
    # We check if the left or right tuple is the one with 0 precedence
    # Then by comparing the components bases to all possible transitions of the other
    # We can verify if the match can be made
    if left[1] == 0:
        return right[0] in transitions[left[0]]
    return left[0] in transitions[right[0]]


main()

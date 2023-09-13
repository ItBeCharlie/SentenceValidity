from enum import Enum


class Basic(Enum):
    PI = 0  # subject
    PI1 = 1  # first person singular subject
    PI3 = 2  # third person singular subject
    PIHAT3 = 3  # pseudo-subject
    S = 4  # declarative sentence, aka statement
    S1 = 5  # statement in present tense
    SBAR = 6  # indirect statement
    I = 7  # infinitive of intransitive verb
    J = 8  # infinitive of complete verb phrase
    O = 9  # direct object
    OHAT = 10  # pseudo-object
    N1 = 11  # count noun

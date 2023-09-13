from basic import Basic as B

dictionary = {
    "john": [(B.PI3, 0)],
    "marie": [(B.PI3, 0)],
    "i": [(B.PI1, 0)],
    "him": [(B.O, 0)],
    "she": [(B.PI3, 0)],
    "will": [(B.PI, 1), (B.S1, 0), (B.J, -1)],
    "come": [(B.I, 0)],
    "see": [(B.I, 0), (B.O, -1)],
    "likes": [(B.PI, 1), (B.S1, 0), (B.O, -1), (B.PIHAT3, 0)],
    # "likes": [(B.PI3, 1), (B.S, 0), (B.PI, -1)],
    "a": [(B.PIHAT3, 1), (B.O, 0), (B.N1, -1)],
    "book": [(B.N1, 0)],
    "which": [(B.N1, 1), (B.N1, 0), (B.OHAT, 0), (B.SBAR, -1)],
    "detests": [(B.PI, 1), (B.SBAR, 0), (B.OHAT, 1)],
    ".": [(B.S, 1)],
}

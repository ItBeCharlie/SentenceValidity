from basic import Basic as B

transitions = {
    B.PI: [B.PI],
    B.PI1: [B.PI1, B.PI],
    B.PI3: [B.PI3, B.PI],
    B.PIHAT3: [B.PIHAT3, B.PI3, B.PI],
    B.S: [B.S],
    B.S1: [B.S1, B.S],
    B.SBAR: [B.SBAR, B.PI3, B.PI],
    B.I: [B.I, B.J],
    B.J: [B.J],
    B.O: [B.O],
    B.OHAT: [B.OHAT, B.O],
    B.N1: [B.N1],
}

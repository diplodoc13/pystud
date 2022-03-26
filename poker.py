# Набросок покера
doc = set()
{doc.add(str(i) + j) for i in range(2, 11) for j in "♠♦♥♣"}
{doc.add(i + j) for i in "JQKA" for j in "♠♦♥♣"}


print("1 Player Hand: ", doc.pop(), doc.pop())
print("2 Player Hand: ", doc.pop(), doc.pop())
print("3 Player Hand: ", doc.pop(), doc.pop())
doc.pop()
flop = [doc.pop(), doc.pop(), doc.pop()]
print("Flop: ", *flop)
doc.pop()
turn = flop + [doc.pop()]
print("Turn: ", *turn)
doc.pop()
river = turn + [doc.pop()]
print("River: ", *river)
print(len(doc))
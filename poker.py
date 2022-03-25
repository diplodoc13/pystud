# Набросок покера
doc = set()
for i in range(2, 11):
    doc.add(str(i) + "D")
    doc.add(str(i) + "H")
    doc.add(str(i) + "C")
    doc.add(str(i) + "S")
for i in ["J", "Q", "K", "A"]:
    doc.add(str(i) + "D")
    doc.add(str(i) + "H")
    doc.add(str(i) + "C")
    doc.add(str(i) + "S")

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
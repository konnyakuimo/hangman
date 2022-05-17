#1
from pyparsing import Word


k="カミュ"
for i in range(3):
    print(k[i])
#2
what=input("何を？")
where=input("どこに？")
print("私は昨日{}を、{}に送った".format(what,where))
#3
print("aldous Huxley wasborn in 1894.".capitalize())
#4
print("だれが？ どこで？ いつ？".split(" "))
#5
words=["The","fox","jumped","over","."]
fox=" ".join(words)
fox=fox.replace(" .",".")
print(fox)
#6
print("A streaming comes across the sky.".replace("s","$"))
#7
print("Hemingway".index("m"))
#8

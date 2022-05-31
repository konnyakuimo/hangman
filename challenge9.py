import csv
#1
with open("st.txt","r",encoding="utf-8") as f:
    print(f.read())
#2
n=str(input("あなたの年齢は？:"))
with open("age.txt","w",encoding="utf-8") as g:
    g.write(n)
with open("age.txt","r",encoding="utf-8") as h:
    print(h.read())
#3
with open("movie.csv","w",encoding="utf-8",newline="") as i:
    w=csv.writer(i,delimiter=",")
    w.writerow(["Top Gun","Risky Buisiness","Minority Report"])
    w.writerow(["Titanic","The Revenant","Inception"])
    w.writerow(["Training Day","Man on Fire","Flight"])
with open("movie.csv","r",encoding="utf-8") as j:
    r=csv.reader(j,delimiter=",")
    for row in r:
        print(",".join(row))

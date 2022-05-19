#1
movie=["ウォーキング・デッド","アントラージュ","ザ・ソプラノズ","ヴァンパイア・ダイアリーズ"]
for movies in movie:
    print(movies)
#2
for i in range(26):
    print(i+25)
    i+=1
#3
j=0
for movies in movie:
    print(j,":",movie[j])
    j+=1
#4
number=["0","5","9"]
print("数字を当てましょう!終了するにはqを入力")
n=str(input("一桁の数字を入力:"))
while n not in number:
    if n=="q":
        print("finish")
        break
    print("違います")
    n=str(input("一桁の数字を入力:"))
    if n in number:
        print("Nice!")
#5
list1=[8,19,148,4]
list2=[9,1,33,83]
newlist=[]
for i in list1:
    for j in list2:
        newlist.append(i*j)
print(newlist)
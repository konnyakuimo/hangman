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
number=["0","5","9","15","27","36","38","41","49"]
while n<=50:
    print("数字を当てましょう!終了するにはqを入力")
    n=str(input("50以下の数字を入力:"))
    if n in number:
        print("正解です")
    else:
        print("違います")
    
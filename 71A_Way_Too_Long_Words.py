n=int(input())
i=0
while i<n:
    i+=1
    w=input()
    if len(w)>10:
        print(f"{w[0]}{len(w)-2}{w[len(w)-1]}")
    else:
        print(w)
magic_square=[
             [8,3,4],
             [1,5,9],
             [6,7,2],]

i=0
while i<len(magic_square):
    sum=0
    j=0
    while j<len(magic_square[i]): 
        sum=sum+magic_square[i][j]
        j=j+1  
    i=i+1
    print(sum)

x=0
while x<len(magic_square):
    s=0
    y=0
    while y<len(magic_square[x]):
        s=s+magic_square[x][y]
        y=y+1
    x=x+1
    print(s,end=" ")
print()
if sum==s:
    print("yes it is magic square")
else:
    print("no it is not magic square")
i=i+1
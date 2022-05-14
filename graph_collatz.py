
def sequence(i):
    func=[]
    i2=i
    done=False
    while not done:
        if i2==1:
            func.append(int(i2))
            done=True
            continue
        if i2%2==0:
            func.append(int(i2))
            i2=i2/2
            continue
        if i2%2==1:
            func.append(int(i2))
            i2=i2*3+1
            continue
    return func

for i in range(1,100): 
    print(sequence(i))
for i in range(1,100):
    print(len(sequence(i)))
for i in range(1,100):
    len1=len(sequence(i))
    str="x"*len1
    print(str)
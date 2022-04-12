# def net_worth(x):
#     for i in range(1000 ):
#         x=.9*x+10
#     print(x)
# # net_worth(150)

x=0
y=0
total_count=0
correct_count=0
while x<10:
    while y<10-x:
        z=10-x-y
        if x+y>z and y+z>x and x+z>y:
            correct_count +=1
        total_count +=1
        y +=.01
        break
    x +=.01
trig_perc=correct_count/total_count
print(trig_perc)
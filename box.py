# width=int(input('Input the width: '))
# height=int(input('Input the height: '))
# long=0
# for vertical in range(height):
#     print('*')

w = 6
h = 4

for i in range(h):
    if not i or i == h-1:
        print('*'*w, end ='')
        print()
    else:
         print('*' + ' '*(w-2) + '*')

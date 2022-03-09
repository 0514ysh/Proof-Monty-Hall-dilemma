import random

k = 0
count = 0
change = 0

num = int(input('반복 횟수 : '))

# 선택을 바꾸지 않을 경우
for i in range(0, num):

    arr = '염소', '염소1', '스포츠카'
    arr2 = []
    
    while len(arr2) < 3 :
        k = random.choice(arr)
        if k not in arr2:
            arr2.append(k)

    for i in range(0,3):
        if arr2[i] == '염소1':
            arr2[i] = '염소'
    
    #print(arr2)
            
    arr3 = [0,1,2]
    choice = random.randint(0,2)
    for i in range(0,3):
        if arr3[i] == choice:
            arr3.remove(arr3[i])
            break
    #print(arr3)
    
    if(arr2[choice] == '스포츠카'): #스포츠카 선택
        count = count +1

        
print('선택을 바꾸지 않았을 경우',num,'번 중 스포츠카를 고른 횟수: ',count,'번')
print('선택을 바꾸지 않았을 경우',num,'번 중 스포츠카를 고를 확률 :',(count/num)*100,'%')

#선택을 바꿨을 경우

count = 0

for i in range(0, num):

    arr = '염소', '염소1', '스포츠카'
    arr2 = []
    
    while len(arr2) < 3 :
        k = random.choice(arr)
        if k not in arr2:
            arr2.append(k)

    for i in range(0,3):
        if arr2[i] == '염소1':
            arr2[i] = '염소'
    
    #print(arr2)
            
    arr3 = [0,1,2]
    choice = random.randint(0,2)
    for i in range(0,3):
        if arr3[i] == choice:
            arr3.remove(arr3[i])
            break
    #print(arr3)
    n = arr3[0]
    m = arr3[1]
    
    if(arr2[n] == '염소'): 
        arr2.remove(arr2[n])
    elif(arr2[m] == '염소'):
        arr2.remove(arr2[m])

    if(arr2[0] == '스포츠카'):
        count = count+1
        
print('선택을 바꾸지 않았을 경우',num,'번 중 스포츠카를 고른 횟수: ',count,'번')
print('선택을 바꾸지 않았을 경우',num,'번 중 스포츠카를 고를 확률 :',(count/num)*100,'%')

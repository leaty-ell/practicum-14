numbers = []
for i in range(10):
    num = int(input())
    numbers.append(num)

new_list=[]
for i in range(1,9): 
    sum_neighbors = numbers[i-1] + numbers[i+1]
    new_list.append(sum_neighbors)

print("Исходный список:", numbers)
print("Новый список:", new_list)


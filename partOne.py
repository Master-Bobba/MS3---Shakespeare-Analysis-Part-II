import re

def twoGrams(nums):

    dic= dict()
    for i in range(len(nums)-1):

        if (nums[i], nums[i+1]) in dic.keys():
            dic[(nums[i], nums[i+1])] += 1
        else:
            dic[(nums[i], nums[i+1])] = 1

    sortedDic= sorted(dic.items(), key=lambda x:x[1], reverse=True)[:10]

    return sortedDic

def threeGrams( nums):

    dic= dict()
    for i in range(len(nums)-2):

        if (nums[i], nums[i+1], nums[i+2]) in dic.keys():
            dic[(nums[i], nums[i+1], nums[i+2])] += 1
        else:
            dic[(nums[i], nums[i+1], nums[i+2])] = 1

    sortedDic= sorted(dic.items(), key=lambda x:x[1], reverse=True)[:10]

    return sortedDic

def fourGrams(nums):

    dic= dict()
    for i in range(len(nums)-3):

        if (nums[i], nums[i+1], nums[i+2], nums[i+3]) in dic.keys():
            dic[(nums[i], nums[i+1], nums[i+2], nums[i+3])] += 1
        else:
            dic[(nums[i], nums[i+1], nums[i+2], nums[i+3])] = 1

    sortedDic= sorted(dic.items(), key=lambda x:x[1], reverse=True)[:10]

    return sortedDic

def fiveGrams(nums):

    dic= dict()
    for i in range(len(nums)-4):

        if (nums[i], nums[i+1], nums[i+2], nums[i+3], nums[i+4]) in dic.keys():
            dic[(nums[i], nums[i+1], nums[i+2], nums[i+3], nums[i+4])] += 1
        else:
            dic[(nums[i], nums[i+1], nums[i+2], nums[i+3], nums[i+4])] = 1

    sortedDic= sorted(dic.items(), key=lambda x:x[1], reverse=True)[:10]

    return sortedDic




name = "pg100.txt"
handle = open(name)

dicTwo = dict()
dicThree = dict()
dicFour = dict()
dicFive = dict()
nums = []


for lines in handle:
    
    for line in lines.split():

        y = re.sub('[^A-Za-z0-9]+', '', line)
        if len(y) > 0:
            nums.append(y)
        

dicTwo = twoGrams(nums)
dicThree = threeGrams(nums)
dicFour = fourGrams(nums)
dicFive = fiveGrams(nums)


print("\nTOP 10 - 2-grams")
i = 1
for word, count in dicTwo:
    print (str(i) + ". " + word[0] + ", " + word[1] +  " -> " + str(count) + " times")
    i += 1

i = 1
print("\nTOP 10 - 3-grams")
for word, count in dicThree:
    print (str(i) + ". " + word[0] + ", " + word[1]+ ", " + word[2]+ " -> " + str(count) + " times")
    i += 1

i = 1
print("\nTOP 10 - 4-grams")
for word, count in dicFour:
    print (str(i) + ". " + word[0] + ", " + word[1] + ", " + word[2] + ", " + word[3] + " -> " + str(count) + " times")
    i += 1

i = 1
print("\nTOP 10 - 5-grams")
for word, count in dicFive:
    print (str(i) + ". " + word[0] + ", " + word[1] + ", " + word[2] + ", " + word[3] + ", " + word[4] + " -> " + str(count) + " times")
    i += 1





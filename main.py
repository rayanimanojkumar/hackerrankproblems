

# reverse string
def reverse_string(sentence):
    words = sentence.split(' ')

    new_word_list = [word[::-1] for word in words]
    res_str = ' '.join(new_word_list)
    return res_str


str1 = 'Read text file'
print(reverse_string(str1))


from collections import OrderedDict
def merge_tools(string, k):
    l = len(string)
    for i in range(0,l,k):
        print(' '.join(OrderedDict.fromkeys(string[i:i+k])))

string = input()
k = int(input())
merge_tools(string,k)


from collections import Counter


def shoes_cost():

    sizes = list(map(int, input('enter the size: ').split(',')))
    n = int(input('enter the customers: '))
    sizes = Counter(sizes)

    total_cost = 0
    for i in range(n):
        size, price = map(int, input('enter the size and price: ').split(','))
        if sizes[size]:
            total_cost += price
            sizes[size] -= 1
    print(total_cost)


shoes = int(input('enter the number of shoes: '))
shoes_cost()

from collections import Counter
def common_char():
    stringN = sorted(input('enter the string: '))
    coun = Counter(stringN).most_common(3)
    for i in coun:
        print(*i)
    return
common_char()

from itertools import product
def maximize():
    n,m = map(int,input('enter the input n amd m: ').split())
    array = []
    for i in range(n):
        array.append(list(map(int, input('enter the list: ').split()))[1:])

    result = 0
    for combination in product(*array):
        result = max(sum([x*x for x in combination]) % m, result)
    print(result)

maximize()



























# def fibonacci(n_terms):
#      n1 = 1
#      n2 = 2
#      count = 0
#      if n_terms<=0:
#          print("enter the positive number.")
#      elif n_terms==1:
#          print(n1)
#      else:
#          print("The fibonacci sequence is: ")
#          while count<n_terms:
#              print(n1, end=' ')
#              n3 = n1+n2
#              n1=n2
#              n2=n3
#              count+=1
#
#
# fibonacci(10)

# def even_fibonacci(num):
#     n1 = 1
#     n2 = 2
#     sum = 0
#     while n2<num:
#         n3=n1+n2
#         n1=n2
#         n2=n3
#         if (n1%2==0):
#             sum+=n1
#     print(sum)
# even_fibonacci(4000000)
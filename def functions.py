# a=[1,2,3,4,5]
# b=[4,5,6,7,8]
# c=[]
# count=0
# d=[]
# for i in a:
#     if i in b:
#         c.append(i)
#         count=+1
#     else:
#         d.append(i)
# for j in b:
#     if j not in a:
#         d.append(j)
# print('elements in both list are{} and its respective count is {}'.format(c,count))
# print('elementsnot in{}'.format(d))
def uppercase_chars(s):
    return [i.upper() for i in s  ]
# str='hello world'
# uppercase=uppercase_chars(str)
print(uppercase_chars('hello world'))
a='helloworld'
b= a.upper()
print(b)
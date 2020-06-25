import re
p = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

email = 'kim@abc.com'

print(p.match(email) != None)
# a = []
# for i in range (10):
#     a.append(i)
# print(a)

# b = [i for i in range(10)]
# print(b)

# for i in range(10):
#     if (1 % 2) == 0:
#         print("짝수")
        
# c = [i for i in range(10) if 1 % 2 == 0]
# dic = {"a":30, "b":20, "c":30}
# tmp_list = ["1","2","3","4","5"]

# for i, val in enumerate(tmp_list):
#     print(i,val)
    
# for i in dic:
#     print(dic.get(i))
# for k, v in dic.items():
#     print(k,v)

a = 'avbc'
b = '1234'
c = '한글'
# print(a.isalpha())
# print(a.isalnum())
# print(b.isdigit())
# print(c.isalnum())
# print(c.isalpha())
# print(c.isascii())

print(a.find("@"))
print(len(b))
import re

# hello1 = "hahaha hello, World !!!"
# hello2 = "hello hahahaha, World"

# print("*"*5 + "match" + "*"*5)
# print(re.match("^hello", hello1))
# print(re.match("^hello", hello2))

# print("\n"+"*"*5 + "search" + "*"*5)
# print(re.search("!!!$", hello1))
# print(re.search("!!!$", hello2))

regex = re.compile('^[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*.[a-zA-Z]{2,3}$')
print(regex.search("lorem_ipsum@gmail.co.kr"))
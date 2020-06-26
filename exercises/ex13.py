# file = open("./data/hello.txt", "w")
# file.write("Hello World !")
# file.close()

import pickle
# hello = "Hello World !"

# # with open('./data/hello.pk1', 'wb') as f:
# #     pickle.dump(hello, f)

# with open('./data/hello.pk1', 'rb') as f:
#     hello = pickle.load(f)
#     print(hello)

hello = {"name": "Hello World !", "gender": "M", "email": "hello@world.com"}

with open('./data/hello.pkl', 'wb') as f:
    pickle.dump(hello, f)
with open('./data/hello.pkl', 'w') as f:
    f.write(hello)

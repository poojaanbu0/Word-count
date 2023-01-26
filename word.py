#Developed by: Pooja a
#Reference Number: 22007907

num_words = 0
with open('text.txt','r') as f1:
    for i in f1:
        word=i.split()
        num_words+=len(word)
print("Number of words in the file={}".format(num_words))
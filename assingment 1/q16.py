#. Write a program in python that counts the frequency of each character in a string.

test_str = "i am learning py"
all_freq = {}
for i in test_str:
    if i in all_freq:
        all_freq[i]+=1
    else :
        all_freq[i]=1
print("count of all characters in :\n"+ str(all_freq))        
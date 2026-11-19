def longestword (word):
    max_length=len(word[])
    for item in word:
        length=len(item)
        if length>max_length:
            max_length=length
            return max_length
words=input("ennnter a lsit of words sepereated by spaces:")
word=words.split()
result=longestword(word)
printf(f"the length of the longest word is:{result}")

s=input("Enter a sentence: ")
print(s)
WordList=s.split()
print(WordList)
uniquewords=set(WordList)
for word in uniquewords:
    print(f"{word} occurs {WordList.count(word)}times")

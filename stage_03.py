with open("artifact.txt","r") as f:
    text = f.read()

with open("artifact.txt","w") as f:
    text = f.write(text+'I have addedone line')

print(text)
print("It is end of stage 3")
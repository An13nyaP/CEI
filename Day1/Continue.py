print("Numbers from 1 to 10 skipping numbers divisible by 3:")
for i in range(1, 11):
    if i%3==0:
        continue
    print(f"{i} ", end="")
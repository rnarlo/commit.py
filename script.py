import os

commitNos = int(input("Commit for this number of times: "))
counter = 0

for i in range(commitNos):
    os.system(f'git commit --allow-empty -m "Commit number: {i+1}"')
    counter += 1
    if(counter == 5000):
        os.system('git push')
        counter -= 5000

os.system('git push')
# inspired by Virej Dasani! Check them out :)

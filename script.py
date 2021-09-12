import os

commitNos = int(input("Commit for this number of times: "))

for i in range(commitNos):
    os.system(f'git commit --allow-empty -m "Commit number: {i+1}"')
    
os.system('git push')

#inspired by Virej Dasani! Check them out :)

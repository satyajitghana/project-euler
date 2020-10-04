import os

dir_li = os.listdir("solutions/")
dir_li.sort()

with open("solutions/solutions.md","w") as f:
    f.write("# Solutions \n" )
    for d in dir_li:
        if "problem" in d:
            f.write(f"* ## [Problem {d[-3:]}]({d}/README.md) \n" )
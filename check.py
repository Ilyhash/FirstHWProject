import subprocess
from difflib import SequenceMatcher
task_array=['vowels','vowels','perfect','perfect','lazy','lazy']
arg_array=['import_antigravity',"You only killed the bride's father, you know. I didn't mean to. Didn't mean to? You put your sword right through his head. Oh dear... is he all right?",'1','15','37','94']


from itertools import tee, islice, chain

def get_also_next_value_in_iterable(some_iterable):
    prevs, items = tee(some_iterable, 2)
    nexts = chain(islice(items, 1, None), [None])
    return zip(prevs, nexts)


flag=True
while flag:
    print("Please enter a file name:")
    file=input()
    if file[-3:] == ".py":
        if not (file[:-3].isdigit()):
            print("File name is invalid! The file name should be your identity number")
        else:
            flag=False

    else:
        if not (file.isdigit()):
            print("File name is invalid! The file name should be your identity number")
        else:
            flag=False
            file += ".py"


# check for allowed libraries
lib = []
try:
    f = open(file)
    for row in f:
        for now_word, next_word in get_also_next_value_in_iterable(row.split()):
            if now_word == "import":
                lib.append(next_word)

except:
    print("file dosn't exist. add it to the test folder")
    exit(0)

lib2 = list(filter(lambda l: l != "argparse", lib))
if len(lib2):
    print("using un-allowed libraries")
    exit(0)


for i in range(6):
    try:
        output_file="output"+str(i+1)+".txt"
        with open(output_file, "w+") as output:
            state = subprocess.call(["python", file, "--task", task_array[i], "--arg", arg_array[i]], stdout=output, );
        file1 = "test/ans"+str(i+1)+".txt"
        file2 = "output"+str(i+1)+".txt"
        text1 = open(file1, 'r', encoding='utf-8', errors='ignore').read()
        text2 = open(file2, 'r', encoding='utf-8', errors='ignore').read()
        m = SequenceMatcher(None, text1, text2)
        if m.ratio() >= 1:
            print("Test Number "+str(i+1)+": Passed")
        elif state==0:
            print("Test Number "+str(i+1)+": Failed")
        else:
            print("Test Number "+str(i+1)+": crashed")
    except:
         print("Test Number "+str(i+1)+": crashed")

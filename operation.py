import sys

def main(args):
    #本当はターミナルで受け取る
    inputpath = "./inputtext.txt"
    outputpath = "./outputtext.txt"

    with open(inputpath) as f:
        contents = f.read()

    if(args[1] == "reverse"):
        reverseContents(contents, outputpath)
    elif(args[1] == "copy"):
        copyContents(contents, outputpath)
    elif(args[1] == "duplicate"):
        duplicateContents(contents, outputpath, int(args[3]))
    elif(args[1] == "replace"):
        replaceContents(contents, outputpath, args[3], args[4])
    
def reverseContents(contents, outputpath):
    """ contentsを逆にして逆順にしたものを新しいファイルに格納 """
    print("execute reverse")
    changedContents = contents[::-1]
    with open(outputpath, "w") as f:
        f.write(changedContents)

def copyContents(contents, outputpath):
    """ contentsをコピーして新しいファイルに格納 """
    print("execute copy")
    with open(outputpath, "w") as f:
        f.write(contents)

def duplicateContents(contents, outputpath, n):
    print("execute duplicate")
    """ cotentsをそのファイルに複製 """
    with open(outputpath, "w") as f:
        f.write(contents + ("\n" + contents) * (n-1)) 

def replaceContents(contents, outputpath, needle, newstring):
    print("execute repalce")
    changedContents = contents.replace(needle, newstring)
    with open(outputpath, "w") as f:
        f.write(changedContents)

main(sys.argv)
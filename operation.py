import sys

def main(args):
    #本当はターミナルで受け取る
    inputpath = args[2]
    outputpath = args[3]

    with open(inputpath) as f:
        contents = f.read()

    if(args[1] == "reverse"):
        reverseContents(contents, outputpath)
    elif(args[1] == "copy"):
        copyContents(contents, outputpath)
    elif(args[1] == "duplicate"):
        duplicateContents(contents, outputpath, int(args[4]))
    elif(args[1] == "replace"):
        replaceContents(contents, outputpath, args[4], args[5])
    
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
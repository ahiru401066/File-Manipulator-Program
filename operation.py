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
        duplicateContents(contents, inputpath, int(args[3]))
    
def reverseContents(contents, outputpath):
    """ contentsを逆にして逆順にしたものを新しいファイルに格納 """
    changedContents = contents[::-1]
    with open(outputpath, "w") as f:
        f.write(changedContents)

def copyContents(contents, outputpath):
    """ contentsをコピーして新しいファイルに格納 """
    with open(outputpath, "w") as f:
        f.write(contents)

def duplicateContents(contents, inputpath, n):
    with open(inputpath, "w") as f:
        f.write(("\n" + contents) * n) 

main(sys.argv)
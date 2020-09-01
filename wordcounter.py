import re

def main():
    print("Welcome to Ana's word counter.")
    dictFile = input("Please enter the name of your dictionary file. i.e. declaration.txt\n")
    try:
        reader = open(dictFile, "r")
        text = reader.read()
        text = text.lower()
        words = re.split('; |, |\n|\.| |\. |,|:',text)
        print(words)
        print(len(words))
        reader.close()
    except:
        print("Coouldn't find your file.. Make sure to put it in the same directory.")
    
    
    
if __name__ == "__main__":
    main()


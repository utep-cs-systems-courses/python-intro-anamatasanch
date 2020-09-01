import re

def main():
    print("Welcome to Ana's word counter.")
    dictFile = input("Please enter the name of your dictionary file. i.e. declaration.txt\n")
    keyFile = input("Please enter the name of your key file.\n")
    ocurrences = {}
    
    try:
        reader = open(dictFile, "r")
        text = reader.read()
        text = text.lower()
        words = re.split('; |, |\n|\.| |\. |,|:|--',text)
        for word in words:
            if len(word)>0:
                if word in ocurrences:
                    ocurrences[word] += 1
                else:
                    ocurrences[word] = 1
        print(sorted(ocurrences.items(), key=lambda item: item[0]))
        reader.close()
    except:
        print("Coouldn't find your file.. Make sure to put it in the same directory.")
    
    
    
if __name__ == "__main__":
    main()


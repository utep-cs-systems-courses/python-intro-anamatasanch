import re

def main():
    print("Welcome to Ana's word counter.")
    dictFile = input("Please enter the name of your dictionary file. i.e. declaration.txt\n")
    keyFile = input("Please enter the name of your key file.\n")
    ocurrences = {}
    
    try:
        reader = open(dictFile, "r")
        text = reader.read()
        reader.close()
        text = text.lower()
        words = re.split('; |, |\n|\.| |\. |,|:|--|-',text)
        
        for word in words:
            if len(word)>0:
                word = word.replace("'", "")
                if word in ocurrences:
                    ocurrences[word] += 1
                else:
                    ocurrences[word] = 1
        sorted_ocurrences = sorted(ocurrences.items(), key=lambda item: item[0])
    except IOError:
        print("Coouldn't find your file.. Make sure to put it in the same directory.")
    
    try:
        f = open(keyFile, "w")
        for ocurrence in sorted_ocurrences:
            f.write(ocurrence[0]+" "+str(ocurrence[1])+"\n")
        f.close()
    except IOError:
        f = open(keyFile, "x")
        for ocurrence in sorted_ocurrences:
            f.write(ocurrence[0]+" "+str(ocurrence[1])+"\n")
        f.close()
    
    
if __name__ == "__main__":
    main()


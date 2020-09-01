def main():
    print("Welcome to Ana's word counter.")
    dictFile = input("Please enter the name of your dictionary file. i.e. declaration.txt\n")
    try:
        reader = open(dictFile, "r")
        print(reader.read())
        reader.close()
    except:
        print("Coouldn't find your file.. Make sure to put it in the same directory.")
    
    
    
if __name__ == "__main__":
    main()


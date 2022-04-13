import sys

def main():
    #Variables
    originalFile = open("SortMe.txt", "r") #The original file we're getting our info from.
    resultFile = open("SortedList.txt", "w+") #The resulting file we're making.
    list = originalFile.readlines() #The original list in array form.
    finalList = [] #The final, resulting list.


    #Clean the list of \n and spaces.
    for i in range(len(list)):
        list[i] = list[i].strip()

    #(I was prepared to figure out an alphabetical sort, but I'll work with what I got.)
    #Sort the list alphabetically
    list = sorted(list)

    #Sort by length, keeping the same, alphabetical, order.
    while len(list) > 0:
        #Make the variables
        smallestValue = len(list[0]) #The size of the smallest string.
        smallestIndex = 0 #The index of the smallest string.
        #Search for the shortest string.
        for j in range(len(list)):
            if(smallestValue > len(list[j])):
                smallestValue = len(list[j])
                smallestIndex = j
        #Stick the shortest at the end of the new list, removing it from the old list.
        finalList.append(list.pop(smallestIndex))

    #If we have a -r argument, reverse it.
    if len(sys.argv) > 1:
        if sys.argv[1] == "-r":
            finalList.reverse()

    #Output to the result file.

    for line in finalList:
        resultFile.write(line + "\n")

    #Close our files.
    resultFile.close()
    originalFile.close()




if __name__ == "__main__":
    main()
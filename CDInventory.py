#--------------------------------------------------------------------#
#Title: Mod05\CDInventory.py
#Description: Lab05-b example solution
#Change Log: (Who, When, What)
#DBisinger, 2030-Jan-01, created file and example solution
#Miroslava Meza,  02/26/2022, reproduced scritp and followed the instructions.
#Miroslava Meza, 02/27/2022. notated where and how to use directories.
#--------------------------------------------------------------------#
#Declare variables

strChoice =''       #user input
lstTbl =[]          #list of lists to hold the data
#TODO 1: creating a data-structure based in dictionaries
dicRow={} #lstRow = [] we substitute with a directory in this example the list of data row
strFileName = 'CDInventory.txt'     #data storage file
objFile = None      #file object

#Get user input
print('The Magic CD Inventory \n')

# Menu with the options available to the user.
while True:
    print('\n[l] Load data from file\n[a] Add data to list\n[w] Write data to file')
    print('[e] Erase an inventory entry\n[d] Display data\n[exit] Quit')
    strChoice = input('l, a, w, e, d, or exit.  ').lower() #convert choice to lower case
    print() #prints a blank row
    
    if strChoice =='exit':
        break 

#-- The first option available in the menu is to load existing data from a file.
# TODO 2: Create teh option of loading existing data.
    if strChoice =='l': # not using elif in this one, bacause is only available if not "exit""
        #open the txt file to print.
        objFile=open(strFileName, 'r') # we are only reading information not writing.
        for row in objFile:
            lstRow= row.strip().split(',')
            dicRow = {'ID': lstRow[0],'Artist': lstRow[1], 'Title': lstRow[2]} #TODO1
            lstTbl.append(dicRow)
        objFile.close()
        for row in lstTbl:
            print(*row.values(), sep =',')
        #I decided not to print the values while the .txt file was open to avoid risk 
        #of corrupting the file. 
        print('If you want to see the current inventory, select \'d\' in the next menu ')
        pass

    elif strChoice  == 'a':
        #Add data to list in memory
        ID=input('Enter the CD Id: ')
        strID=str(ID)
        strArtist = input('Enter the CD\'s artist: ')
        strTitle = input('Enter the CD\'s Title: ')
        #Creating the keys for a dictionary.
        dicRow= {'ID': strID, 'Artist': strArtist, 'Title': strTitle}#TODO1
        #Each new dictionary entry will be append to lstTbl
        lstTbl.append(dicRow)
        #let the user know that their changes are saved only in temporary memory and reminds them to 
        # use the option Write to save later.
        print('your current changes are saved in temporary memory,\nsave your changes into the external txt file by choosing [w] from the main menu')
        pass #added this item from the original starter file.

    elif strChoice=='w':
        #write from list to data file
        objFile=open(strFileName, 'w')  # I did not use the 'a' function because
                                        #the user had the opportunity to load the vaues of
                                        #the existing values. If they chose not to, this allows
                                        #to start all over from zero. If they want to append, they can just use l
        for row in lstTbl:
            strRow=''
            for item in row.values():
                strRow += str(item) + ','
            strRow = strRow[:-1]+'\n'
            objFile.write(strRow)
        objFile.close()
        #letting the user know that the all their new entries have been added to 
        # the external txt file.
        print('All your recent entries and/or deletions have been saved to the file CDInventory.txt')
        pass

    elif strChoice =='e':
# TODO 3: 
      
        # 1--- Display updated data to identify the row
        print('Identify the row you want to erase, count top from bottom and type the row number \n')
        print('ID, Artist, Title')
        for row in lstTbl:
            print(*row.values(), sep = ',')
   # Request the row to erase, The data is a list form, thus whatever the user 
   # provides shoud be ((row_input)-1)
        eraselist2=int(input('Write the number of row you want removed from your inventory: '))
        i=eraselist2-1 # the list starts in [0].
        lstTbl.remove(lstTbl[i])
#----Write into txt file
        objFile=open(strFileName, 'w')  # I did not use the 'a' function because
                                        #the user had the opportunity to load the vaues of
                                        #the existing values. If they chose not to, this allows
                                        #to start all over from zero. If they want to append, they can just use l
        for row in lstTbl:
            strRow=''
            for item in row.values():
                strRow += str(item) + ','
            strRow = strRow[:-1]+'\n'
            objFile.write(strRow)
        objFile.close()
        
        pass

    elif strChoice =='d':
        #Display data
        print('ID, Artist, Title')
        for row in lstTbl:
            print(*row.values(), sep = ',')
        pass

    else:
        print('Please choose either l, a, w, e, d, or exit. ')
        pass
    
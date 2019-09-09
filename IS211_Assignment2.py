#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""Week 2 Assignment 
Python modules from the Standard Library """

import urllib.request
import urllib.error
import logging
import argparse
import datetime 



#url = 'https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv'


#Part 2

def downloadData(url):
    """ Function takes in a string called url
        to download the contents located at the url and return it to the caller"""

    data1 = urllib.request.urlopen(url).read().decode("ascii","ignore")
    return data1

#Part 3
def processData(datafile):

    """ Function returns a dictionary that maps a person’s ID to a tuple """

    csv_file = csv.reader(data)
    my_dict = {}
    csv_file.next()
    
    for row in csv_file:
        try:
            row[2] = datetime.datetime.strptime(row[2], "%d/%m/%Y").date()
            
        except ValueError:
                number = int(row[0])
                line = int(row[0])+1
                logger = logging.getLogger("assignment 2")
                logger.error("Error processing line#{} for ID #{}.".format(line, number))
                
        my_dict[int(row[0])] = (row[1], row[2])                                 
    return my_dict
  

#Part 4

def displayPerson(id, personData):

    """ Function prints the name and birthday of a given user identified by the input id. 
    If there is not entry with the given id, then print “No user found with that id” instead. """    
                                          
    try:

        response = "Person ID #{idnum} is {name} with a birthday of {date}"
        print(response.format(idnum=id, name=personData[id][0], date=personData[id][1]))

    except KeyError:
        print("An error on Person ID # entered.")



#Part 5


def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help = "URL to csv file.", type=str)
    args = parser.parse_args()
    logging.basicConfig(filename="errors.log", level = logging.ERROR)
    
    
    if args.url:
        file_Data = downloadData(args.url)
        personData = processData(file_Data)
        msg = "Please enter an ID# for lookup or 0 or a negative # to exit. "
        
        while True:
            
            try:
                
                user = int(raw_input(msg))
            except urllib.error.URLError as e:
                 print( "URL error. ", e.reason)
            except ValueError: 
                print("URL not valid. Please enter a valid URL or type 0 or a negative # to exit.")
                continue
            if user > 0:
                print("You have entered: "), user
                displayPerson(user, personData)

            else:

                print("You have entered: "), user
                print("Program will now exit.")
                system.exit()

    else:
        
        print("Please enter URL.")

if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:





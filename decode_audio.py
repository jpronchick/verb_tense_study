import csv
import base64
import os

def readFile(filename):
    
    csv.field_size_limit(300000) # for big csv
    
    # Column locations for each category of data
    AUDIO = 2
    TRIAL_TAG = 4
    PROMPT = 5
    ITEMNUM = 6
    LIST = 7
    FRAGMENT = 8
    ADJ = 9
    ID = 13
    
    with open(filename, newline='') as csvfile:         # creates a file object
        csvreader = csv.reader(csvfile, delimiter=',')  # set for reading csv file
        
        next(csvreader)                                 # skips header
        
        for row in csvreader:                           # read data
           # if(row[STIMTYPE]!="filler"):                #skip fillers
            writeFiles(os.path.basename(filename), 
                       decodeAudio(row[AUDIO]), row[TRIAL_TAG], 
                       row[ID])
        
def decodeAudio(audioEncoded):
    return base64.b64decode(audioEncoded)
    
def writeFiles(filename, audioDecoded, trial_tag, PID):
    newFname = f'{trial_tag}_{PID}.wav'
    #newFname = newFname.replace('/', '-') #the '/' is not allowed in filenames, this line saves some data cleanup
    if not(os.path.isdir(f'newaudioData/{filename}')):
        os.mkdir(f'newaudioData/{filename}')
    f = open(f'newaudioData/{filename}/{newFname}', 'wb')
    f.write(audioDecoded)
    f.close()

def main():
    for file in os.listdir("newDataVerbTense"):
        if not (file.startswith(".")):          #skip hidden files
          readFile(f'newDataVerbTense/{file}')
            

    
main()
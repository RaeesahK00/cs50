import csv                  #import csv to allow us to read and process csv files
import sys                  #import sys so that we can handle comand-line arguments


def main():

    if len(sys.argv) != 3:                                                  #Check if the correct command-line argument is provided
        print("Usage error python dna.py databases/.csv sequences/.txt")    #print out the usage error message
        sys.exit(1)                                                         #exit out of the program

    csv_file = sys.argv[1]                              #assigning the comand-line arguments to variables
    sequence_file = sys.argv[2]



    with open(csv_file) as file:                        #read database file into a variable
        csv_reader = csv.DictReader(file)               #converts each row in the csv file into a dictionary where the keys are columns
        str_sequences = csv_reader.fieldnames[1:]       #skipping the first variable which is "name"
        single_sequences = list(csv_reader)             #stores the database as lists of dictionaries, showing each individual DNA profile eg. {Alice , AGATC..} {James, AATG...} etc.


    with open(sequence_file) as file:                   #read DNA sequence file into a variable
        dna_sequence = file.read()


    str_counter = {}                                                        # initialize str_counter to a ldictionary to store the counts of the longest runs
    for sequences in str_sequences:                                         # loop through the list
        str_counter[sequences] = longest_match(dna_sequence,sequences)      # find longest match of each STR in DNA sequence


    for names in single_sequences:                                  #check database for matching profiles
        matching_profile = True                                     #assign/flagging matching_profile as True

        for i in str_sequences:                             #loop through the list
            if int(names[i]) != str_counter[i]:             #check if names is equal to the counter string
                matching_profile = False                    #if true assign matching_profile to false
                break                                       #break out of loop when false
        if matching_profile:                                #if matching_profile is true
            print(names['name'])                            #print out the name of the

    print("No match")                                       #print no match when nothing passes the




def longest_match(sequence, subsequence):                   #returns length of longest run of subsequence in sequence

                                                            #initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)


    for i in range(sequence_length):                        #check each character in sequence for most consecutive runs of subsequence

        count = 0                                           #initialize count of consecutive runs

                                                            #check for a subsequence match in a "substring" (a subset of characters) within sequence
                                                            #if a match, move substring to next potential match in sequence
        while True:                                         #continue moving substring and checking for matches until out of consecutive matches
            start = i + count * subsequence_length          #adjust substring start and end
            end = start + subsequence_length

            if sequence[start:end] == subsequence:          #if there is a match in the substring
                count += 1
            else:                                           #if there is no match in the substring
                break

        longest_run = max(longest_run, count)               #update most consecutive matches found

    return longest_run                                      #after checking for runs at each character in seqeuence, return longest run found

main()                                                      #call the main method

import question_b

def main():

    user_option = 0

    while(user_option != 2):

        print("*******************")
        print("Where in the string is it?")
        print("1-Find the location(s) of your subDNA in the DNA.")
        print("2-Exit")
        print("*******************")
    
        user_option = input("Make a selection: ")

        if (user_option == '1'):

            dna_string1 = input("Enter a DNA string: ").upper()

            while (len(dna_string1) < 8 or len(dna_string1) >= 16):
                dna_string1 = input("Enter a DNA string: ").upper()

            dna_string2 = input("Enter your DNA substring: ").upper()

            while (len(dna_string2) != 4):
                dna_string2 = input("Enter your DNA substring: ").upper()

            locations = question_b.get_most_likely_ancestor_consensus(dna_string1, dna_string2)

            print("Here are the index locations of your DNA substring in the main DNA: ")
            for i in locations:
                print(i)

            print("----------------------------------")
          
            end_run = '0'
            
            while (end_run != 'y'):
                end_run = input("Do you want to exit: Y or N? ")
                    
                if (end_run == 'y' or end_run == 'Y'):
                    print("Exiting....")
                    break
                    
                elif (end_run == 'n' or end_run == 'N'):
                    print("Continuing...")
                    break
                else:
                    print("Invalid response. Do you want to exit: Y or N?")

            if (end_run == 'y' or end_run == 'Y'):
                break
            else:
                continue

        elif (user_option == '2'):
            
            end_run = '0'
            
            while (end_run != 'y'):
                end_run = input("Do you want to exit: Y or N? ")
                    
                if (end_run == 'y' or end_run == 'Y'):
                    print("Exiting....")
                    break
                    
                elif (end_run == 'n' or end_run == 'N'):
                    print("Continuing...")
                    break
                else:
                    print("Invalid response. Do you want to exit: Y or N?")

            if (end_run == 'y' or end_run == 'Y'):
                break
            else:
                user_option = '0'
                continue

        else:
            print("*******************")
            print("Invalid menu option")

main()
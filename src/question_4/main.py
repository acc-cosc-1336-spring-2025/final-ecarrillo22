import question_d

def main():

    user_option = 0

    while(user_option != 2):

        print("*******************")
        print("Stock List")
        print("1-Display Stock List")
        print("2-Exit")
        print("*******************")

        user_option = input("Make a selection: ")

        if (user_option == '1'):
            
            stock_list = question_d.get_stock_list()
            stock_list

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
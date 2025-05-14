#write functions here, don't add input('') statements here!
def test_config():
    return True

def get_multiplication_table(rows, cols):
    list = [] #multiplication main list

    for r in range(0, rows):
        mult_row_list = []

        for c in range(0, cols):
            mult_row_list.append((r + 1) * (c + 1))

        list.append(mult_row_list)

    return list

def display_multiplication_table(list):

    for row_list in list:
        for item in row_list:
            print(str(item).rjust(3, " "), end = " ")
        
        print(" ")
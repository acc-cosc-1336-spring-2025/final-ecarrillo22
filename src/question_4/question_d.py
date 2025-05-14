class Stock:

    def __init__(self, symbol, company_name):
        self.__symbol = symbol
        self.__company_name = company_name

    def get_symbol(self):
        return self.__symbol
    
    def get_company_name(self):
        return self.__company_name

def get_stock_list():
    file = open('stock_file.dat', 'w')

    stock_list = [['AAPL', 'Apple'], ['CAT', 'Caterpillar'], ['EK', 'Eastman Kodak'], ['GOOG', 'Google'], ['MSFT', 'Microsoft']]

    for stock in stock_list:
        file.write(stock[0] + '\t')
        file.write(stock[1] + '\n')

    file.close()

    file = open('stock_file.dat', 'r')

    stocks = []

    for line in file:
        record = line.split('\t')
        symbol = record[0]
        company = record[1].rstrip('\n')

        stocks_list = [symbol, company]

        stocks.append(stocks_list)
    
    print(f"{'Symbol':<10} {'Company Name'}")
    for stock in stocks:
        print(f"{stock[0]:<10} {stock[1]}")

    file.close()
class Stock:

    def __init__(self, symbol, company_name):
        self.__symbol = symbol
        self.__company_name = company_name

    def get_symbol(self):
        return self.__symbol
    
    def get_company_name(self):
        return self.__company_name
    
def stock_purchase_history():

    stock1 = Stock('AAPL', 'Apple Inc')
    stock2 = Stock('CAT', 'Caterpillar')
    stock3 = Stock('EK', 'Eastman Kodak')
    stock4 = Stock('GOOG', 'Google')
    stock5 = Stock('MSFT', 'Microsoft')

    stock_dict = {}

    stock_dict[stock1.get_symbol()] = stock1.get_company_name()
    stock_dict[stock2.get_symbol()] = stock2.get_company_name()
    stock_dict[stock3.get_symbol()] = stock3.get_company_name()
    stock_dict[stock4.get_symbol()] = stock4.get_company_name()
    stock_dict[stock5.get_symbol()] = stock5.get_company_name()

    print(f"{'Symbol':<10} {'Company Name'}")
    for symbol, company in stock_dict.items():
        print(f"{symbol:<10} {company}")
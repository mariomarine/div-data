import csv

import yfinance as yf

KEEP_KEYS = ['beta','dividendRate','dividendYield','fiftyDayAverage','ficeYearAvgDividendYield','forwardPE','industry','logo_url','shortName','marketCap','payoutRatio','pegRatio','profitMargins','priceToBook','priceToSalesTrailing12Months','sector','shortRatio','symbol','trailingAnnualDividendRate','trailingAnnualDividendYield','twoHundredDayAverage','volume','yield']

def filter_info(info, keep):
    return dict(filter(lambda elem: elem[0] in keep, info.items()))

def make_safe(value):
    return value.encode('utf8') if isinstance(value, basestring) else value

def write_dict_to_csv(info_dict):
    keys = info_dict[0].keys()
    with open('utilities_info.csv', 'wb') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        for row in info_dict:
            try:
                dict_writer.writerow({k:make_safe(v) for k,v in row.items()})
            except Exception as e:
                print("This row errored")
                print(e)
                print(row)

def get_info(ticker):
    stock = yf.Ticker(ticker)
    try:
        info = filter_info(stock.info, KEEP_KEYS)
        return info
    except:
        return {}

def main():
    all_info = []
    with open('utilities.txt') as f:
        for line in f:
            ticker = line.strip()
            info = get_info(ticker)
            if info:
                all_info.append(info)
    write_dict_to_csv(all_info)

if __name__ == '__main__':
    main()

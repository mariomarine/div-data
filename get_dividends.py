import csv

import yfinance as yf

def flatten_and_enhance_dict(item, ticker, action_type):
    return {'Date': item[0], 'Amount': item[1], 'Stock': ticker, 'Type': action_type}

def write_dict_to_csv(action_dict):
    keys = action_dict[0].keys()
    with open('utilities.csv', 'wb') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(action_dict)

def main():
    all_actions = []
    with open('utilities.txt') as f:
        for line in f:
            ticker = line.strip()
            stock = yf.Ticker(ticker)
            actions = stock.actions.to_dict()
            divs = [flatten_and_enhance_dict(x, ticker, 'Dividend') for x in actions['Dividends'].items() if x[1] != 0]
            splits = [flatten_and_enhance_dict(x, ticker, 'Split') for x in actions['Stock Splits'].items() if x[1] != 0]
            final_actions = divs + splits
            all_actions = all_actions + final_actions
    write_dict_to_csv(all_actions)

if __name__ == '__main__':
    main()

import csv

import yfinance as yf

def mod_divs(dividends, modifier):
    for i, div in enumerate(dividends):
        dividends[i].update({'Amount': float(div['Amount'])/modifier})
    return dividends

def modify_dividends(div_history):
    splits = [i for i, e in enumerate(div_history) if e['Type'] == 'Split']
    if len(splits) > 0:
        modified_dividends = mod_divs(div_history[0:splits[0]], div_history[splits[0]]['Amount'])
        div_history = modify_dividends(modified_dividends + div_history[splits[0]+1:])
    return div_history

def flatten_and_enhance_dict(item, ticker, action_type):
    return {'Date': item[0], 'Amount': item[1], 'Stock': ticker, 'Type': action_type}

def write_dict_to_csv(action_dict):
    keys = action_dict[0].keys()
    with open('utilities.csv', 'wb') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(action_dict)

def get_actions(ticker):
    stock = yf.Ticker(ticker)
    actions = stock.actions.to_dict()
    divs = [flatten_and_enhance_dict(x, ticker, 'Dividend') for x in actions['Dividends'].items() if x[1] != 0]
    splits = [flatten_and_enhance_dict(x, ticker, 'Split') for x in actions['Stock Splits'].items() if x[1] != 0]
    final_actions = divs + splits
    return modify_dividends(final_actions)

def main():
    all_actions = []
    with open('utilities.txt') as f:
        for line in f:
            ticker = line.strip()
            all_actions = all_actions + get_actions(ticker)
    write_dict_to_csv(all_actions)

if __name__ == '__main__':
    main()

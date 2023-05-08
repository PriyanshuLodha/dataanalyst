import math

import pandas as pd
  
# Load the data of csv

df = pd.read_csv('tradelog.csv')


# Define initial portfolio value and risk-free interest rate
initial_portfolio_value = 200000
risk_free_rate = 0.05

# Define list of trades
trades = [...] # list of trades goes here

# Calculate total number of trades
total_trades = len(trades)

# Calculate number of profitable trades
profitable_trades = len([trade for trade in trades if trade['profit_loss'] > 0])

# Calculate number of loss-making trades
loss_making_trades = total_trades - profitable_trades

# Calculate win rate
win_rate = profitable_trades / total_trades

# Calculate average profit per trade
average_profit = sum([trade['profit_loss'] for trade in trades if trade['profit_loss'] > 0]) / profitable_trades

# Calculate average loss per trade
average_loss = sum([trade['profit_loss'] for trade in trades if trade['profit_loss'] < 0]) / loss_making_trades

# Calculate risk reward ratio
risk_reward_ratio = abs(average_profit / average_loss)

# Calculate expectancy
loss_rate = 1 - win_rate
expectancy = (win_rate * average_profit) - (loss_rate * average_loss)

# Calculate average ROR per trade
total_return = sum([trade['profit_loss'] for trade in trades])
volatility = math.sqrt(sum([(trade['profit_loss'] - (total_return / total_trades)) ** 2 for trade in trades]) / (total_trades - 1))
average_ror_per_trade = (total_return / total_trades - risk_free_rate) / volatility

# Calculate sharpe ratio
sharpe_ratio = average_ror_per_trade / volatility

# Calculate max drawdown
max_drawdown = 0
peak_value = initial_portfolio_value
for trade in trades:
    peak_value = max(peak_value, peak_value + trade['profit_loss'])
    drawdown = peak_value - (initial_portfolio_value + sum([t['profit_loss'] for t in trades[:trades.index(trade)+1]]))
    max_drawdown = min(max_drawdown, drawdown)

# Calculate max drawdown percentage
max_drawdown_percentage = (max_drawdown / initial_portfolio_value) * 100

# Calculate CAGR
ending_value = initial_portfolio_value + total_return
num_periods = (trades[-1]['exit_time'] - trades[0]['entry_time']).days / 365
cagr = (ending_value / initial_portfolio_value) ** (1/num_periods) - 1

# Calculate calmar ratio
calmar_ratio = abs(cagr / max_drawdown_percentage)

# Print results
print(f"Total Trades: {total_trades}")
print(f"Profitable Trades: {profitable_trades}")
print(f"Loss-Making Trades: {loss_making_trades}")
print(f"Win Rate: {win_rate:.2%}")
print(f"Average Profit per trade: {average_profit:.2f}")
print(f"Average Loss per trade: {average_loss:.2f}")
print(f"Risk Reward Ratio: {risk_reward_ratio:.2f}")
print(f"Expectancy: {expectancy:.2f}")
print(f"Average ROR per trade: {average_ror_per_trade:.2f}")
print(f"Sharpe Ratio: {sharpe_ratio:.2f}")
print(f"Max Drawdown: {

# Risk and position size calculator for buying shares

# Get account details
acc_size = float(input("Enter your account size: "))
risk_per_trade = float(input("Enter risk per trade (%): "))

# Get entry and stop-loss prices
entry_price = float(input("Enter entry price: "))
stop_loss = float(input("Enter stop-loss price: "))

# Check that the inputs are valid
if acc_size <= 0 or not (0 < risk_per_trade <= 100):
    print("Account size must be positive and risk must be between 0 and 100%.")

elif not (0 < stop_loss < entry_price):
    print("Stop-loss must be positive and below the entry price.")

else:
    # Calculate the percentage drop from entry to stop-loss
    stop_loss_percent = ((entry_price - stop_loss) / entry_price) * 100

    # Calculate the amount of money at risk
    risk_amount = acc_size * (risk_per_trade / 100)

    # Calculate position value based on the risk budget
    pos_size = risk_amount / (stop_loss_percent / 100)

    # Limit the position to the available account balance
    pos_size = min(pos_size, acc_size)

    # Round down to whole shares
    shares = int(pos_size / entry_price)

    # Calculate position value and risk after rounding
    position_value = shares * entry_price
    planned_risk = shares * (entry_price - stop_loss)

    # Display results with two decimal places
    print(f"Stop-loss distance: {stop_loss_percent:.2f}%")
    print(f"Risk budget: ${risk_amount:.2f}")
    print(f"Number of shares: {shares}")
    print(f"Position value: ${position_value:.2f}")
    print(f"Planned risk at stop-loss: ${planned_risk:.2f}")
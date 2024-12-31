import requests

def get_conversion_rate(from_currency, to_currency, amount):
    
    url = "https://exchange-rate-api1.p.rapidapi.com/latest"
    
    querystring = {"base":from_currency.upper()}
    
    headers = {
        "x-rapidapi-key": "",
        "x-rapidapi-host": "exchange-rate-api1.p.rapidapi.com"
        }

    response = requests.get(url, headers=headers, params=querystring)
    with open("exchange_rate.json", "w") as f:
        f.write(response.text)
    print(response.json())
    rate = response.json()["rates"][to_currency.upper()]
    print(f"1 {from_currency} is equal to {rate} {to_currency}")
    
    converted_amount = amount * rate
    print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")
    return converted_amount

class BankAccount:
    def __init__(self, holder_first_name, holder_last_name, holder_address, initial_balance, currency="USD"):
        self.balance = initial_balance
        self.holder_first_name = holder_first_name
        self.holder_last_name = holder_last_name
        self.holder_address = holder_address
        self.currency = currency
        print(self.__dict__)

    def converted_amount(self, amount, currency):
        return get_conversion_rate(self.currency, currency, amount)
        
    def deposit(self, amount, currency="USD"):
        if currency != self.currency:
            amount = self.converted_amount(amount, currency)
            if amount > 0:
                self.balance += amount
                print(f"Deposited ${amount}. Your Current balance is ${self.balance}")
                return True
            else:
                print("Invalid deposit amount. Please deposit a positive value.")
                return False
                
    def withdraw(self, amount, currency="USD"):
        if currency != self.currency:
            amount = self.converted_amount(amount, currency)
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. Your Current balance is ${self.balance}")
            return True
        else:
            print("Invalid withdrawal amount. Please withdraw a positive value that is less than your balance.")
            return False
        
    def get_balance(self):
        return self.balance

    
account = BankAccount("John", "Doe", "123 Main St", 100)

account.deposit(50)
account.deposit(100, "EUR")
account.withdraw(30)
print("Current balance:", account.get_balance())
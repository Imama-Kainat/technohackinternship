from currency_converter import CurrencyConverter


def main():
    print("This is a currency converter project.")
    print("You can use these currencies (INR, PKR,USD, EUR, JPY)")

    amount = float(input("Enter the amount you want to convert: "))
    curr_currency = input("Enter the currency which you currently have: ").upper()
    want_currency = input("Enter the currency to which you want to convert: ").upper()

    # Correct the typo in the class name: CurrencyConverter
    c = CurrencyConverter()
    converted_amount = c.convert(amount, curr_currency, want_currency)

    # Use print(f) formatied string, correct format string for displaying the result
    print(f"The {amount} {curr_currency} is: {converted_amount} {want_currency}")


# #main()
# from currency_converter import CurrencyConverter
#
# print("This is a currency converter project.")
# print("You can use these currencies ( PKR, INR,USD, EUR, JPY)")
#
# amount = float(input("Enter the amount you want to convert: "))
# curr_currency = input("Enter the currency which you currently have: ").upper()
# want_currency = input("Enter the currency to which you want to convert: ").upper()
#
# # Correct the typo in the class name: CurrencyConverter
# c = CurrencyConverter()
# converted_amount = c.convert(amount, curr_currency, want_currency)
#
# # Use print(f) formatted string, correct format string for displaying the result
# print(f"The {amount} {curr_currency} is: {converted_amount} {want_currency}")

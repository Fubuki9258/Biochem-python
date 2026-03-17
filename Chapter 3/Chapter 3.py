"""
Chapter 3: Basics
"""

print("(3 + 6) / (3 *2) is equal to", (3 + 6) / (3 *2))
print("\n7//2 is equal to", 7//2, "and the remainder is", 7%2)
print("\nTo distinguish between odd and even numbers, we can do floor division by 2, and check the remainder." \
"\nIf the remainder is 1, the number is odd, if the remainder is 0, the number is even.")

print("He said: \"I don't like John O\'Mill at all\".")

# help(), help> indicates that the help function is still active

# Think Python, section 2.10, part 2 of 2.2
cover_price = 24.95 # price of book in USD
bookstore_discount = 0.6 # 40% discount means we pay 60% of the price
shipping = 3 #shipping cost in USD for the first copy
additional_shipping = 0.75 #shipping cost for each additional copy in USD
number_of_copies = 60

# Calculate the total wholesale cost for 60 copies of the book, including the discount and shipping costs.
# Round float off to 2 decimals
print("\nThe total wholesale cost for", number_of_copies, "copies is:",
      round((cover_price * bookstore_discount * number_of_copies) + shipping + (additional_shipping * (number_of_copies - 1)), 2), "USD")
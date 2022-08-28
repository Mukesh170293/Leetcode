from Array.BestTimeToBuyAndSellStock import maxProfit
from Array.contains_duplicate import contains_Duplicate
from Array.contains_duplicateii import contains_duplicate_ii
from Math.AddDigits import add_digits
from Math.Bulbswitcher import buld_switcher
from Math.Codec import Codec
from Math.plaindrone import isPalindrome
from Math.plusone import plusOne
def buy_and_sell_stocks(prices):
    print(maxProfit(prices))

def contains_duplicate_I(nums):
    print(contains_Duplicate(nums))

def contains_duplicate_II(nums, k):
    print(contains_duplicate_ii(nums, k))

def adddigits(num):
    print(add_digits(num))

def buld_switcher_output(num):
    print(buld_switcher(num))

def short_and_long_url(url):
    codec = Codec()
    print(codec.decode(codec.encode(url)))

def palindrone(number):
    print(isPalindrome(number))

def plus_one(number):
    print(plusOne(number))


if __name__ == '__main__':
    plus_one([9,9,9])


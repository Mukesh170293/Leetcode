from Array.BestTimeToBuyAndSellStock import maxProfit
from Array.contains_duplicate import contains_Duplicate
from Array.contains_duplicateii import contains_duplicate_ii
from Math.AddDigits import add_digits
from Math.Bulbswitcher import buld_switcher
from Math.Codec import Codec
from Math.plaindrone import isPalindrome
from Math.plusone import plusOne
from Math.poorpigs import poorPigs
from Math.poweroftwo import isPowerOfTwo
from Math.missing_number import missingNumber
from Backtracking.permuatation import permute
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

def poor_pigs_count(buckets, minutesToDie, minutesToTest):
    print(poorPigs(buckets, minutesToDie, minutesToTest))

def PowerOfTwo(n):
    print(isPowerOfTwo(n))

def missing_number_output(nums):
    print(missingNumber(nums))

def permute_list(nums):
    print(permute(nums))

if __name__ == '__main__':
    permute_list([1,2,3,4])


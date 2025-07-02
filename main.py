"""
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that
the majority element always exists in the array.
169/Array
"""
import random
from collections import Counter, defaultdict
from math import gcd, floor

# n = int(input("Size if List:"))
# list_ = []
#
# for i in range(n):
#     k = int(input('>>>'))
#     list_.append(k)
# print(max(list_, key=lambda x: list_.count(x)))
# sorted(list_ , key=lambda x : list_.count(x))[-1]


"""
Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.
709/string
"""
# s = 'Hello'
# new = ""
# for char in s:
#     if char.isupper():
#         new += char.lower()
#     else:
#         new += char
# print(new)

"""
You are given a string title consisting of one or more words separated by a single space, where each word consists of
English letters. Capitalize the string by changing the capitalization of each word such that:
If the length of the word is 1 or 2 letters, change all letters to lowercase.
Otherwise, change the first letter to uppercase and the remaining letters to lowercase.
Return the capitalized title.
2129
"""
# title = "First leTTeR of EACH Word"
# res = []
# for word in title.split(" "):
#     if len(word) <= 2:
#         res.append(word.lower())
#     else:
#         res.append(word.capitalize())
# new = " ".join(res)
# print(new)

"""
You are given a large integer represented as an integer array digits, where each digits[i] is 
the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. 
The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.
66/Array
"""

# digits = [1,2,9]
# res = "".join(str(i) for i in digits)
# result = int(res) + 1
# my_list = [int(digit) for digit in str(result)]
# print(my_list)

"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, 
also represented as a string.
Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
Array/ 43
# """
# num1, num2 = "123", "456"
# print(str(int(num1) * int(num2)))


"""

Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.
String // 58
"""
# s = "   fly me   to   the moon  "
# my_list = [word for word in s.split()]
# print(len(my_list[-1]))


"""
Given a string s, reverse the order of characters in each word within a sentence while 
still preserving whitespace and initial word order.
String //557
"""
# s = "Let's take LeetCode contest"
# result = []
# for word in s.split():
#     result.append(word[::-1])
# print(" ".join(result))

"""
Given a string s and an integer k, reverse the first k characters for every 2k characters counting 
from the start of the string.
If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or 
equal to k characters, then reverse the first k characters and leave the other as original.
String //541
"""
# s = "abcdefg"
# k = 2
# result = ""
# j = True
# for i in range(len(s)//k+1):
#     if j:
#         result += s[i*k:i*k+k][::-1]
#         j = False
#     else:
#         result += s[i*k:i*k+k]
#         j = True
# print(result)
#

"""
Given two strings a and b, return the length of the longest uncommon subsequence between a and b.
If no such uncommon subsequence exists, return -1.
An uncommon subsequence between two strings is a string that is a 
subsequence of exactly one of them.
String // 521
a= "aefawfawfawfaw", b="aefawfeawfwafwaef"
https://leetcode.com/problems/longest-uncommon-subsequence-i/description/?envType=problem-list-v2&envId=string
"""
# a, b = "aefawfawfawfaw", "aefawfeawfwafwaef"
# if a == b:
#     print(-1)
# else:
#     print(max(len(a), len(b)))


"""
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
You must solve the problem without using any built-in library for handling large integers (such as BigInteger). 
You must also not convert the inputs to integers directly
string / 415
"""
# num1 = "19"
# num2 = "123"
# maxx = max(num1, num2, key = len)
# minn = min(num2, num1, key = len)
# minn = minn.zfill(len(maxx))
# carry = 0
# summ = []
# for i in range(len(maxx) -1, -1, -1):
#     res = int(maxx[i]) + int(minn[i]) + carry
#     if res >= 10:
#         carry = 1
#         res -= 10
#     else:
#         carry = 0
#     summ.append(str(res))
# if carry:
#     summ.append(str(carry))
# result = "".join(summ[::-1])
# print(result)


'''
Paskal uchburchagining dastlabki n ta qatorini toping.
'''
# n = int(input('Number:'))
# r = [1]
# paskal =[r]
#
# for i in range(n-1):
#     tmp = []
#     for j in range(len(r)-1):
#         tmp.append(sum(r[j:j+2]))
#     tmp = [1] + tmp + [1]
#     paskal.append(tmp)
#     r = tmp
# print(paskal)

# ----------------------------------------------------------------
# def generate_row(prev):
#     next_row = [1]
#     for i in range(len(prev) -1):
#         next_row.append(prev[i] + prev[i+1])
#     next_row.append(1)
#     return next_row
# def generate(n):
#     if n == 0:
#         return []
#     row = [1]
#     pascal = [row]
#     for i in range(n -1):
#         row = generate_row(row)
#         pascal.append(row)
#     return pascal
# n = 5
# print(generate(n))

"""
numsKamaymaydigan tartibda tartiblangan butun sonlar massivi berilgan bo‘lsa , 
berilgan targetqiymatning boshlang‘ich va yakuniy pozitsiyasini toping.
Agar targetmassivda topilmasa, qaytaring [-1, -1].
Ish vaqti murakkabligi bilan algoritm yozishingiz kerak  O(log n).
Array//34
# """
# nums = [5,7,7,8,8,10]
# target = 8
# res = []
# try:
#     res.append(nums.index(target))
#     for i in range(len(nums) -1, -1, -1):
#         if nums[i] == target:
#             res.append(i)
#             break
# except:
#     res = [-1,-1]
# print(res)


"""
Turli xil butun sonlarning tartiblangan massivi va maqsad qiymatini hisobga olgan holda, agar maqsad topilsa, 
indeksni qaytaring. Agar yo'q bo'lsa, indeksni tartibda kiritilsa, qayerda bo'lishini qaytaring.
Ish vaqti murakkabligi bilan algoritm yozishingiz kerak  O(log n).
Array//35
"""
# nums = [1,3,5,6]
# target = 7
# try:
#     print(nums.index(target))
# except:
#     nums.append(target)
#     nums = sorted(nums)
#     print(nums.index(target))

"""
Alohida butun sonlar massivi berilgan bo'lsa nums, barcha mumkin bo'lganlarni qaytaring
almashtirishlar. Javobni istalgan tartibda qaytarishingiz mumkin .
Array//46
# """
from itertools import permutations, repeat, combinations, combinations_with_replacement, chain, count

# nums = [1,1,2]
# res = []
# per = permutations(nums)
# for p in per:
#     res.append(list(p))
# print(res)

"""
Ikki nusxani o'z ichiga olishi mumkin bo'lgan raqamlar to'plamini hisobga olgan holda , 
barcha mumkin bo'lgan noyob almashtirishlarni istalgan tartibdanums qaytaring 
Array // 47.
# """
# nums = [1,1,2]
# res = []
# per = permutations(nums)
# for p in per:
#     if not p in res:
#         res.append(tuple(p))
# print(list(set(res)))


"""561 //Array
https://leetcode.com/problems/array-partition/description/?envType=problem-list-v2&envId=array
"""
from itertools import permutations

# nums = [6,2,6,5,1,2]
# nums.sort()
# pairs = []
# for i in range(0, len(nums), 2):
#     pairs.append((nums[i], nums[i+1]))
# print(sum(pair[0] for pair in pairs))]

"""
Array//136
https://leetcode.com/problems/single-number/?envType=problem-list-v2&envId=array
"""
# nums = [2,2,1,3,3]
# for key, value in Counter(nums).items():
#     if value == 1:
#         print(key)

"""Hash table
https://leetcode.com/problems/intersection-of-two-arrays/description/?envType=problem-list-v2&envId=hash-table
"""
# nums1 = [4,9,5]
# nums2 = [9,4,9,8,4]
# print(list(set(nums1).intersection(set(nums2))))


"""Hash table
https://leetcode.com/problems/majority-element/description/?envType=problem-list-v2&envId=hash-table
eng ko'p uchragan element qaysiki >= u [n/2]
"""
# nums = [3,2,2,1,2,1,1,1] # [1,1,1,1,2,2,2,3]
# in this case this approach doesn't work
# nums.sort()
# print(nums[len(nums) // 2])
#
# print(Counter(nums).most_common()[0][0])


"""
https://leetcode.com/problems/find-the-difference/description/?envType=problem-list-v2&envId=string
"""
# s = "abcd"
# t = "abecd"
# s = sorted(s)
# t = sorted(t)
# for i in range(len(s)):
#     if s[i] != t[i]:
#         print(t[i])
#         break
# else:
#     print(t[-1])


"""Hash Table
https://leetcode.com/problems/intersection-of-two-arrays-ii/description/?envType=problem-list-v2&envId=hash-table
"""
# [4,9,9]
# nums1 = [4,9,9,9,5]
# nums2 = [9,4,9,8,4]
# count1 = Counter(nums1)
# count2 = Counter(nums2)
# result = []
# for num , quantity in count1.items():
#     if num in count2:
#         result += [num]*min(count2.get(num) , quantity)
# print(result)

"""
https://leetcode.com/problems/reverse-string/description/?envType=problem-list-v2&envId=string
"""
# s = ["h","e","l","l","o"]
# print(s.reverse())

'''
https://leetcode.com/problems/most-common-word/description/?envType=problem-list-v2&envId=hash-table
'''
# paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
# banned = ["hit"]
# # paragraph = "a, a, a, a, b,b,b,c, c"
# # banned = ["a"]
# paragraph.replace(" ",'').split().lower().translate(str.maketrans('', "", string.punctuation))
# most_common_words = Counter(paragraph).most_common()
# print(most_common_words)
# for word in most_common_words:
#     if word[0] not in banned:
#         print(word[0])
#         break

"""
https://leetcode.com/problems/reverse-vowels-of-a-string/description/
"""
# s = list("leetcode")
# res = []
# for i , char in enumerate(s):
#     if char in ['a', 'u', 'e', 'i','o', 'A', 'U', 'E', 'I','O']:
#         res.append(char)
#         s[i] = "{}"
# print("".join(s).format(*res[::-1]))
"""
https://leetcode.com/problems/valid-palindrome/description/?envType=problem-list-v2&envId=string
"""
# s = "A man, a plan, a canal: Panama"
# s = "".join(s.translate(str.maketrans(" ", " ", string.punctuation )).lower().split())
# print( s[0:] == s[::-1])

"""
https://leetcode.com/problems/odd-string-difference/description/?envType=problem-list-v2&envId=string
"""
import string

# words = ["adc", "wzy", "abc"]
# words = ["aaa","bob","ccc","ddd"]
# words_ = []
# difference = []
# for word in words:
#     tmp=[]
#     for i in range(0, len(word) - 1):
#         tmp.append(ord(word[i+1]) - ord(word[i]))
#     difference.append(tmp)
#     index = difference.index(min(difference,word.count()))
#     print(index)
# #======================================================================
# for i, word in enumerate(words):
#     diff = ord(words[0]) - ord('a')
#     tmp = ''
#     for char in word:
#         tmp += chr(ord(char) - diff)
#     words_.append(tmp)
# index = words_.index(min(words_, key=words_.count()))
# print(words[index])

"""
https://leetcode.com/problems/truncate-sentence/description/?envType=problem-list-v2&envId=string
"""
# s = "Hello how are you Contestant"
# k = 4
# print(" ".join(s.split()[:k]))

"""
https://leetcode.com/problems/rotate-string/description/?envType=problem-list-v2&envId=string
"""
# s = "abcde"
# goal = "cdeab"
# print(len(s) == len(goal)  and goal in s + s)

"""
https://leetcode.com/problems/check-if-the-sentence-is-pangram/description/?envType=problem-list-v2&envId=string
"""
# sentence = "thequickbrownfoxjumpsoverthelazydog"
# print(len(set(sentence)) == 26)

"""
https://leetcode.com/problems/count-pairs-of-similar-strings/description/?envType=problem-list-v2&envId=string
"""
# words = ["aba","aabb","abcd","bac","aabc"]
# res = [set(word)for word in words]

"""
https://leetcode.com/problems/find-common-characters/description/?envType=problem-list-v2&envId=string
"""
# words = ["bella","label","roller"]
# res = Counter(words[0])
# for word in words:

"""
https://leetcode.com/problems/greatest-common-divisor-of-strings/description/?envType=problem-list-v2&envId=string
"""
# str1 = "ABABAB"
# str2 = "CDF"
# if str1 + str2 != str2 + str1:
#     print("")
# else:
#     index = gcd(len(str1), len(str2))
#     maxx = max(str1, str2, key = len)
#     print(maxx[:index])

"""
https://leetcode.com/problems/occurrences-after-bigram/description/?envType=problem-list-v2&envId=string
"""
# text = "we will we will rock you"
# first = "we"
# second = "will"
# text = text.split()
# res = []
# for i in range(len(text)-1):
#     if text[i] == first  and text[i+1] == second:
#         res.append(text[i+2])
# print(res)

"""
https://leetcode.com/problems/defanging-an-ip-address/?envType=problem-list-v2&envId=string
"""
# address = "1.1.1.1"
# print(address.replace('.', '[.]'))
#
# print("[.]".join(address.split('.')))

"""
https://leetcode.com/problems/move-zeroes/description/?envType=problem-list-v2&envId=array
"""
# nums = [0,1,0,3,12]
# for num in nums:
#     if num == 0:
#         nums.append(num)
#         nums.remove(num)
# print(nums)

"""
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/?envType=problem-list-v2&envId=array
"""

# nums = [4,3,2,7,8,2,3,1]
# set_nums = set(nums)
# res = []
# for num in list(range(1,len(nums)+1)):
#     if num not in set_nums:
#         res.append(num)
# print(res)


"""
https://leetcode.com/problems/minimum-absolute-difference/description/?envType=problem-list-v2&envId=array
"""
# arr = [4,5,1,3]
# sorted_arr = sorted(arr)
# length = len(sorted_arr)
# min_difference = sorted_arr[1] - sorted_arr[0]
# print(min_difference)
# for i in range(2, length):
#     min_difference = min(min_difference, sorted_arr[i] - sorted_arr[i-1])
# print(min_difference)
# res = []
# for i in range(length):
#     if sorted_arr[i] - sorted_arr[i-1] == min_difference:
#         res.append([sorted_arr[i], sorted_arr[i-1]])
# print(res)

"""
https://leetcode.com/problems/shuffle-the-array/description/?envType=problem-list-v2&envId=array
"""
# nums = [2,5,1,3,4,7]
# n = 3
# arr1 = nums[0:n]
# arr2 = nums[n:]
# res = []
# print(arr1)
# print(arr2)
# for i in range(len(arr1)):
#     res.append([arr1[i], arr2[i]])
# print([i for item in res for i in item])


"""
https://leetcode.com/problems/number-of-good-pairs/description/?envType=problem-list-v2&envId=array
"""
# nums = [1,2,3,1,1,3]
# nums = [1,1,1,1]
# count = 0
# for num in list(Counter(nums).values()):
#     count += (num * (num -1))//2
# print(count)

"""
https://leetcode.com/problems/number-of-changing-keys/description/?envType=problem-list-v2&envId=string
"""
# s = "aAbBcC"
# s = s.lower()
# count = 0
# for i in range(len(s)-1):
#     if s[i] != s[i+1]:
#         count += 1
# print(count)

"""
https://leetcode.com/problems/valid-word/description/
"""
# word = "234Adas"
# word = 'UuE6'
# vowels = 'aeuioAEUIO'
# v_count =0
# c_count =0
# if len(word) < 3:
#     print(False)
# else:
#     if word.isalnum():
#         for char in word:
#             if char.isalpha() and char in vowels:
#                 v_count += 1
#             if char.isalpha() and char not in vowels:
#                 c_count += 1
#     else:
#         print(False)
# if c_count >= 1 and v_count >= 1:
#     print(True)
# else:
#     print(False)

"""
https://leetcode.com/problems/final-value-of-variable-after-performing-operations/description/?envType=problem-list-v2&envId=string
"""
# operations = ["--X","X++","X++"]
# x = 0
# d ={
#     '--X' : -1,
#     '++X': +1,
#     'X--': -1,
#     'X++': +1
# }
# for operation in operations:
#     if operation in ('--X', 'X--'):
#         x += d[operation]
#     else:
#         x += d[operation]
# print(x)

"""
https://leetcode.com/problems/shuffle-string/description/?envType=problem-list-v2&envId=string
"""
# s = "abc"
# indices = [0,1,2]
# res = []
# for i in range(len(s)):
#     res.append((s[i], indices[i]))
# res = sorted(res, key= lambda x: x[1])
# string = ""
# for l in [x for r in res for x in r]:
#     if str(l).isalpha():
#         string += l
# print(string)

"""
https://leetcode.com/problems/sorting-the-sentence/description/?envType=problem-list-v2&envId=string
"""
# s = "is2 sentence4 This1 a3"
# sorted_ = sorted(s.split(), key=lambda x: x[-1])
# print(" ".join(word[:-1] for word in sorted_))

"""
https://leetcode.com/problems/replace-all-digits-with-characters/description/?envType=problem-list-v2&envId=string
"""
# s = "a1b2c3d4e"
# res = ""
# letters = string.ascii_lowercase
# start = letters.index(s[0])
# for char in s:
#     if char.isdigit():
#         res += letters[start+ int(char)]
#     else:
#         res += char
#     start = letters.index(res[-1])
# print(res)

"""
https://leetcode.com/problems/sum-of-unique-elements/description/?envType=problem-list-v2&envId=hash-table
"""
# nums = [1,1,1,1]
# sum = 0
# for key, value in Counter(nums).items():
#     if value == 1:
#         sum += int(key)
# print(sum)

"""
https://leetcode.com/problems/sort-the-people/description/?envType=problem-list-v2&envId=hash-table
"""
# names = ["Mary","John","Emma"]
# heights = [180,165,170]
# names = ["Alice","Bob","Bob"]
# heights = [155,185,150]
# res = []
# for i in range(len(names)):
#     res.append([names[i], heights[i]])
# print(res)
# sorted_ = sorted(res, key=lambda x: x[-1], reverse=True)
# print(sorted_)
# print([i for item in sorted_ for i in item][::2])

"""
https://leetcode.com/problems/squares-of-a-sorted-array/description/?envType=problem-list-v2&envId=array
"""
# nums = [-4,-1,0,3,10]
# res = []
# for num in nums:
#     res.append(num **2)
# print(sorted(res))

"""
https://leetcode.com/problems/shift-2d-grid/description/
"""
# grid = [[1,2,3],[4,5,6],[7,8,9],[1,2,3]]
# l = len(grid[0])
# print(l)
# k = 1
# matrix = list(chain(*grid))
# k_ = k % len(matrix)
# rotate = matrix[-k_:] + matrix[:-k_]
# print([rotate[i:i + l] for i in range(0, len(rotate), l)])

"""
https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/?envType=problem-list-v2&envId=hash-table
"""
# nums = [7,1,5,4,3,4,6,0,9,5,8,2]
# res = []
# for i, val in Counter(nums).items():
#     if val == 2:
#         res.append(i)
# print(res)
# seen = set()
# for num in nums:
#     if num in seen:
#         res.append(num)
#     seen.add(num)
# print(res)

"""
https://leetcode.com/problems/points-that-intersect-with-cars/description/?envType=problem-list-v2&envId=hash-table
"""
# nums = [[3,6],[1,5],[4,7]]
# res = set()
# [res.update(set(range(row[0], row[1]+1))) for row in nums]
# print(len(res))

# s = "dfa11111afd"
# res = set()
# for char in s:
#     if char.isdigit():
#         res.add(int(char))
# try:
#     print(sorted(res)[-2])
# except:
#     print(-1)

"""
https://leetcode.com/problems/fair-candy-swap/description/?envType=problem-list-v2&envId=hash-table
"""
# sum(aliceSizes)-x+y == sum(bobsize)-y+x
# aliceSizes = [2]
# bobSizes = [1,3]
# res = []
# l = max(aliceSizes, bobSizes)
# for i in range(0,len(l)-1):
#     x = aliceSizes[i]
#     y = bobSizes[i]
#     aliceSizes.remove(x)
#     bobSizes.remove(y)
#     if aliceSizes.append(y) == bobSizes.append(x):
#         res.append([aliceSizes[i], bobSizes[i]])
# if res:
#     print(res[0])
# else:
#     print(res)

"""
https://leetcode.com/problems/minimum-common-value/description/?envType=problem-list-v2&envId=hash-table
"""
# nums1 = [1, 2, 3]
# nums2 = [2, 4]
# nums1 = [1000000000,1000000000]
# nums2 = [1000000000]
# l = set(nums1).intersection(nums2)
# print(min(l))
# paths =[["pYyNGfBYbm","wxAscRuzOl"],["kzwEQHfwce","pYyNGfBYbm"]]
# s = {i[0] for i in paths}
# f = {i[1] for i in paths}
# print(f.difference(s).pop())
#
"""
https://leetcode.com/problems/distance-between-bus-stops/?envType=problem-list-v2&envId=array
"""
# distance = [7,10,1,12,11,14,5,0]
# start = 7
# destination = 2
#
# if start > destination:
#     line1 = sum(distance[destination : start])
#     line2 = sum(distance[start:] + distance[:destination])
#     print(min(line1, line2))
# else:
#     line1 = sum(distance[start: destination])
#     line2 = sum(distance[destination:] + distance[:start])
#     print(min(line1 , line2))
#
# """
# https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/description/?envType=problem-list-v2&envId=array
# """
# sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
# print(max(sentence.count(" ") for sentence in sentences) + 1)

"""
https://leetcode.com/problems/keep-multiplying-found-values-by-two/description/?envType=problem-list-v2&envId=array
"""
# nums = [2,7,9]
# original = 3
# while original:
#     if original in nums:
#         original *= 2
#     else:
#         break
# print(original)
"""
https://leetcode.com/problems/find-target-indices-after-sorting-array/description/?envType=problem-list-v2&envId=array
"""
# nums = [1,2,5,2,3]
# target = 6
# nums = sorted(nums)
# res = []
# for i, num in enumerate(nums):
#     if num == target:
#         res.append(i)
# print(res)
# =============================================
# left = 0
# right = len(nums) -1
# while left <= right:
#     mid = (left + right) // 2
#     if target == nums[mid]:
#         res.append(mid)
#     elif target < nums[mid]:
#         right = mid -1
#     else:
#         left = left + 1
# print(res)

"""
https://leetcode.com/problems/count-common-words-with-one-occurrence/description/?envType=problem-list-v2&envId=array
"""
# words1 = ['a', 'ab']
# words2 = ["a","a","a","ab"]
# c1 = Counter(words1)
# c2 = Counter(words2)
# count = 0
# for key, val in c1.items():
#     if key in c2.keys() and val == c2[key] == 1:
#         count += 1
# print(count)
"""
https://leetcode.com/problems/count-the-number-of-consistent-strings/description/?envType=problem-list-v2&envId=string
"""
# allowed = "ab"
# words = ["ad","bd","aaab","baa","badab"]
# count = 0
# for word in words:
#     if set(word).issubset(allowed):
#         count += 1
# print(count)

"""
https://leetcode.com/problems/goal-parser-interpretation/submissions/1532281478/?envType=problem-list-v2&envId=string
"""
# command = "(al)G(al)()()G"
#
# res = []
# i = 0
# while i < len(command):
#     if command[i] == "G":
#         res.append("G")
#         i +=1
#     elif command[i:i+2] == "()":
#         res.append('o')
#         i += 2
#     elif command[i:i+4] == "(al)":
#         res.append('al')
#         i += 4
# print("".join(res))

"""
https://leetcode.com/problems/merge-strings-alternately/description/?envType=problem-list-v2&envId=string
"""
# word1 = "ab"
# word2 = "pqcd"
# res = []
# l1 = len(word1)
# l2 = len(word2)
# minn = min(l1, l2)
#
#
# for i in range(minn):
#     res.append(word1[i])
#     res.append(word2[i])
# if l1 > l2:
#     res.append(word1[minn:])
# else:
#     res.append(word2[minn:])
# print("".join(res))

"""
https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/description/?envType=problem-list-v2&envId=string
"""
# firstWord,secondWord ,targetWord = "acb",  "cba", "cdb"
# letters = 'abcdefghij'
# def word_to_num(word):
#     num = ""
#     for char in word:
#         num += str(letters.index(char))
#     return int(num)
# f_ = word_to_num(firstWord)
# s_ = word_to_num(secondWord)
# t_ = word_to_num(targetWord)
# print(f_ + s_ == t_)

"""
https://leetcode.com/problems/number-of-senior-citizens/description/?envType=problem-list-v2&envId=string
"""
# details = ["7868190130M7522","5303914400F9211","9273338290F4010"]
# count = 0
# ages =[word[-4:-2] for word in details]
# for age in ages:
#     if int(age) > 60:
#         count += 1
# print(count)
# ======================
# for detail in details:
#     if int(detail[-4:-2]) > 60:
#         count += 1
# print(count)

"""
https://leetcode.com/problems/find-the-difference-of-two-arrays/?envType=problem-list-v2&envId=hash-table
"""
# nums1 = [1,2,3]
# nums2 = [2,4,6]
# res  = []
# res.append(list(set(nums1).difference(nums2)))
# res.append(list(set(nums2).difference(nums1)))
# print(res)

"""
https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/description/?envType=problem-list-v2&envId=hash-table
"""
# s = "abacbc"
# print(len(set(Counter(s).values())) == 1)


"""
https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/description/?envType=problem-list-v2&envId=hash-table
"""
from itertools import permutations

# nums = [3,2,1,5,4]
# k = 2
# count = 0
# for num in list(combinations(nums,2)):
#     if abs(num[0] - num[1]) == k:
#         count += 1
# print(count)


"""
https://leetcode.com/problems/find-lucky-integer-in-an-array/?envType=problem-list-v2&envId=hash-table
"""
# arr = [2,2,3,4]
# # arr = [1,2,2,3,3,3]
# res = []
# for key, val in Counter(arr).items():
#     if key == val:
#         res.append(key)
# if res:
#     print(max(res))
# else:
#     print(-1)

"""
https://leetcode.com/problems/uncommon-words-from-two-sentences/submissions/1533368601/?envType=problem-list-v2&envId=hash-table
"""
# s1 = "apple apple"
# s2 = "banana"
# new = s1 +" "+ s2
# c = Counter(new.split())
# print(c)
# res = []
# for key, val in c.items():
#     if val == 1:
#         res.append(key)
# print(res)


""""
https://leetcode.com/problems/determine-color-of-a-chessboard-square/description/?envType=problem-list-v2&envId=string
"""
# coordinates = "c7"
# letters = "abcdefgh"
# d = {
#     'a': 1,
#     'b': 2,
#     'c': 3,
#     'd': 4,
#     'e': 5,
#     'f': 6,
#     'g': 7,
#     'h': 8
# }
# res = []
# if coordinates[0] in d.keys():
#     res.append([d.get(coordinates[0]),int(coordinates[1])])
# res = list(chain(*res))
# if res[0] == res[1]:
#     print(False)
# elif res[0] % 2 != 0 and res[1] % 2 != 0:
#     print(False)
# elif res[0] % 2 == 0 and res[1] % 2 == 0:
#     print(True)
# elif res[0] % 2 == 0 and res[1] % 2 != 0:
#     print(True)
# elif res[0] % 2 != 0 and res[1] % 2 == 0:
#     print(True)

"""
https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/description/?envType=problem-list-v2&envId=string
"""
# s = "aababcabc"
# count = 0
# for i in range(len(s) - 2):
#     print(s[i:i+3])
#     if len(set(s[i:i+3])) == 3:
#         count += 1
# print(count)

"""
https://leetcode.com/problems/fizz-buzz/description/?envType=problem-list-v2&envId=string
"""
# n = 15
# nums = [num for num in range(1,n+1)]
# res = []
# print(nums)
# for num in nums:
#     if num % 3 == 0 and num % 5 == 0:
#         res.append('FizzBuzz')
#     elif num % 3 == 0 and num % 5 != 0:
#         res.append('Fizz')
#     elif num % 5 == 0 and num % 3 != 0:
#         res.append('Buzz')
#     else:
#         res.append(str(num))
# print(res)

"""
https://leetcode.com/problems/detect-capital/description/?envType=problem-list-v2&envId=string
"""
# word = "asa"
# l = len(word)
# count =0
# if word.islower():
#     print(True)
# else:
#     for i in range(l):
#         if word[i].isupper():
#             count += 1
#     if l == count:
#         print(True)
#     elif count == 1 and word[0].isupper():
#         print(True)
#     else:
#         print(False)
#
# def int_to_roman(num):
#     val = [
#         (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
#         (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
#         (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
#     ]
#
#     roman_numeral = ""
#     for value, symbol in val:
#         while num >= value:
#             roman_numeral += symbol
#             num -= value
#     return roman_numeral
#
#
# # Example usage:
# print(int_to_roman(844))

"""
https://leetcode.com/problems/relative-ranks/description/?envType=problem-list-v2&envId=array
"""
# score = [10,3,8,9,4]
# l = len(score)
# res = [""] * l
# d = {}
# for index, val in enumerate(score):
#     d[val] = index
# print(d)
# score.sort(reverse=True)
# print(score)
# for i in range(l):
#     if i == 0:
#         res[d[score[i]]] = 'Gold Medal'
#     elif i == 1:
#         res[d[score[i]]] = 'Silver Medal'
#     elif i == 2:
#         res[d[score[i]]] = 'Bronze Medal'
#     else:
#         res[d[score[i]]] = str(i + 1)
# print(res)

# even_nums = (x for x in range(10) if x % 2 == 0)
# while True:
#     try:
#         print(next(even_nums))
#     except StopIteration:
#         break

"""
https://leetcode.com/problems/maximum-product-of-three-numbers/description/?envType=problem-list-v2&envId=array
"""
from math import prod

# nums = [-100,-98,-1,2,3,4]
# combs = combinations(nums, 3)
# print(prod(max(combs, key=lambda x: prod(x))))

"""
https://leetcode.com/problems/first-bad-version/description/
"""

# class Solution:
#     def firstBadVersion(self, n: int) -> int:
#         start, end = 1, n
#         while start <= n:
#             mid = (start + end) // 2
#             if isBadVersion(mid):
#                 end = mid -1
#             else:
#                 start = mid + 1
#         return start

"""
https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/description/?envType=problem-list-v2&envId=binary-search
"""
# nums = [-1,1,2,3,1]
# nums = [-6,2,5,-2,-7,-1,3]
# target = -2
# combs = combinations(nums,2)
# res =[x for x in combs if sum(x) < target]
# print(len(res))

"""
https://leetcode.com/problems/check-if-n-and-its-double-exist/description/?envType=problem-list-v2&envId=binary-search
"""
# arr = [-2,0,10,-19,4,6,-8]#[10,2,5,3]
# nums = arr.copy()
# for i in nums:
#     if i == 0 and arr.count(0) == 1:
#         continue
#     if i * 2 in arr:
#         print(True)
#         break
# else:
#     print(False)

"""
https://leetcode.com/problems/determine-if-string-halves-are-alike/description/?envType=problem-list-v2&envId=string
"""
# s = "textbook"
# l = len(s)//2
# a = s[:l]
# b = s[l:]
# count_a,count_b = 0, 0
# for i in range(l):
#     if a[i] in 'aeuioAEUIO':
#         count_a += 1
#     if b[i] in 'aeuioAEUIO':
#         count_b += 1
# print(count_b == count_a)

"""
https://leetcode.com/problems/reformat-date/description/?envType=problem-list-v2&envId=string
"""
# date = "2th Oct 2052"
# data1 = date.split()
# months = {"Jan": '01',
#           "Feb": '02',
#           "Mar": '03',
#           "Apr": "04",
#           "May": '05',
#           "Jun": '06',
#           "Jul": '07',
#           "Aug": '08',
#           "Sep": '09',
#           "Oct": '10',
#           "Nov": '11',
#           "Dec": '12'
#           }
#
# day = data1[0][:2] if data1[0][1].isdigit() else "0" + data1[0][0]
# print("-".join([data1[-1], months[data1[1]], day]))

"""
https://leetcode.com/problems/maximum-number-of-words-you-can-type/description/?envType=problem-list-v2&envId=string
"""
# text = "hello world"
# brokenLetters = "ad"
# count = 0
# for t in text.split():
#     r = 0
#     for char in t:
#         if char not in brokenLetters:
#             r += 1
#     if len(t) == r:
#         count += 1
# print(count)

"""
https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/?envType=problem-list-v2&envId=string
"""
# patterns = ["a","abc","bc","d"]
# word = "abc"
# count = 0
# for pattern in patterns:
#     if pattern in word:
#         count += 1
# print(count)

"""
https://leetcode.com/problems/number-of-lines-to-write-string/description/?envType=problem-list-v2&envId=string
"""
# widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
# s = "abcdefghijklmnopqrstuvwxyz"
# zipped = dict(zip(string.ascii_lowercase, widths))
# print(zipped)
# count = 1
# summ = 0
# for i in s:
#     if summ + zipped[i] > 100:
#         count += 1
#         summ = 0
#     summ += zipped[i]
# print(count, summ)

"""
https://leetcode.com/problems/rotate-string/description/?envType=problem-list-v2&envId=string
"""
# s = "abcde"
# goal = "abcde"
# if s == goal:
#     print(True)
# else:
#     i = 1
#     while i < len(s):
#         s = s[-1]+s[:-1]
#         if s== goal:
#             print(True)
#             break
#         i += 1
#     print(False)

"""
https://leetcode.com/problems/reverse-only-letters/description/?envType=problem-list-v2&envId=string
"""
# s = "ab-cd"
# s = list(s)
# print(s)
# res = []
# for i, index in enumerate(s):
#     if i in string.ascii_letters:
#         res.append(i)
#         s[index] = "{}"
# print("".join(s).format(*res[::-1]))

""

""
# arr = ["d","b","c","b","c","a"]
# k = 2
# distinct = [i for i in arr if arr.count(i) == 1]
# if len(distinct) < k:
#     print(" ")
# else:
#     print(distinct[k-1])

"""
https://leetcode.com/problems/two-out-of-three/?envType=problem-list-v2&envId=array
"""
# nums1 = [1,1,3,2]
# nums2 = [2,3]
# nums3 = [3]
#
# nums1 = list(set(nums1))
# nums2 = list(set(nums2))
# nums3 = list(set(nums3))
# res = nums1 + nums2 + nums3
# res1 = []
# for key, val in Counter(res).items():
#     if val >= 2:
#         res1.append(key)
#
# print(res1)

"""
https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/?envType=problem-list-v2&envId=array
# """
# # words = ["hello","world","leetcode"]
# # chars = "welldonehoneyr"
# words = ["cat","bt","hat","tree"]
# chars = "atach"
# chars_count = defaultdict(int)
# for char in chars:
#    chars_count[char] += 1
#
# w_count = defaultdict(int)
# for word in words:
#     for w in word:
#          w_count[w] += 1
# result = 0
# flag = True
# for key, val in w_count.items():
#     if val <= chars_count[key]:
#         flag = False
#         break
# if flag:
#     result += len(word)
# print(result)

"""
https://leetcode.com/problems/find-first-palindromic-string-in-the-array/description/?envType=problem-list-v2&envId=string
"""
# words = ["abc","car","ada","racecar","cool"]
# for word in words:
#     if word == word[::-1]:
#         print(word)
#         break
#     else:
#         print("")

"""
https://leetcode.com/problems/counting-words-with-a-given-prefix/?envType=problem-list-v2&envId=string
"""
# words = ["pay", "attention", "practice", "attend"]
# pref = "at"
# count = 0
# for word in words:
#     if word.startswith(pref):
#         count += 1
# print(count)

"""
https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/description/?envType=problem-list-v2&envId=string
"""
# s = "1 box has 3 blue 4 red 6 green and 12 yellow marbles"
# res = []
# for i in s.split():
#     if i.isdigit():
#         res.append(int(i))
# print(res == sorted(set(res)))

"""
https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/description/?envType=problem-list-v2&envId=string
"""
# s = "aabb"
# b = 'ba'
# print(b not in s)

"""
https://leetcode.com/problems/sum-of-digits-of-string-after-convert/description/?envType=problem-list-v2&envId=string
"""
# letters = string.ascii_lowercase
# s = "leetcode"
# k = 2
# nums = ""
# for i in s:
#     nums += str(letters.index(i)+1)
# i = 0
# while i< k:
#     nums = str(sum(int(num) for num in nums))
#     i += 1
# print(nums)

"""
https://leetcode.com/problems/running-sum-of-1d-array/description/?envType=problem-list-v2&envId=array
"""
# nums = [1,1,1,1,1]
# nums = [3,1,2,10,1]
# new = []
# for i in range(1,len(nums)):
#     new.append(sum(nums[:i]))
# new.append(sum(nums))
# print(new)

"""
https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/description/?envType=problem-list-v2&envId=array
"""
# nums = [1,5,4,5]
# nums.sort()
# print((nums[-2] - 1) * (nums[-1] - 1))

"""
https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/?envType=problem-list-v2&envId=array
"""
# candies = [2,3,5,1,3]
# extraCandies = 3
# candies = [4,2,1,1,2]
# extraCandies = 1
# candies_ = candies.copy()
# res = []
# for i in range(len(candies)-1):
#     candies[i] = candies[i] + extraCandies
#     res.append((max(candies) == candies[i]))
#     candies[i] = candies_[i]
#     print(candies[i])
# res.append(candies_[-1] + extraCandies >= max(candies_))
#
# print(res)
"""
https://leetcode.com/problems/find-numbers-with-even-number-of-digits/description/?envType=problem-list-v2&envId=array
"""
# nums = [12,345,2,6,7896]
# count = 0
# for num in nums:
#     if len(str(num)) % 2 == 0:
#         count += 1
# print(count)

"""
https://leetcode.com/problems/sum-of-good-numbers/description/?envType=problem-list-v2&envId=array
"""
# nums = [1,3,2,1,5,4]
# k = 2

"""
https://leetcode.com/problems/rank-transform-of-an-array/description/?envType=problem-list-v2&envId=array
"""
# arr = [37,12,28,9,100,56,80,5,12]
# copy_arr = arr.copy()
# d = {}
# for index, val in enumerate(sorted(set(copy_arr))):
#     if  val in d.keys():
#         continue
#     else:
#         d[val] = index + 1
# print(d)
# res = []
# for i in arr:
#     if i in d.keys():
#         res.append(d.get(i))
# print(res)

# =============================================================================
"""
https://leetcode.com/problems/unique-number-of-occurrences/description/?envType=problem-list-v2&envId=array
"""
# arr = [1,2,2,1,1,3]
# c = Counter(arr)
# print(len(c.values()) ==  len(set(c.values())))


# ========================================================
"""
https://leetcode.com/problems/special-array-i/description/?envType=problem-list-v2&envId=array
"""
# nums = [4,3,1,6]
# if len(nums) == 1:
#     print(True)
# else:
#     for i in range(len(nums)-1):
#         if nums[i] % 2 == 0 and nums[i + 1] % 2 == 0:
#             print(False)
#             break
#         elif nums[i] % 2 != 0 and nums[i + 1] % 2 != 0:
#             print(False)
#             break
#     print(True)

# """
# 3151
# """
# # nums = [6,3,9]
# # print(len(list(filter(lambda x: x % 3 != 0, nums))))
#
# """
# 1374 / string
# """
# n = 4
# if n % 2 != 0:
#     print('a' * 4)
# else:
#     print('a' * (n-1) + 'b')

"""
https://leetcode.com/problems/count-items-matching-a-rule/description/?envType=problem-list-v2&envId=string
"""
# items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
# ruleKey = "color"
# ruleValue = "silver"


"""
https://leetcode.com/problems/reverse-prefix-of-word/description/?envType=problem-list-v2&envId=string
"""
# word = "abcdefd"
# ch = "d"
# index = word.index(ch)
# f_part = word[:index + 1]
# print(f_part[::-1]+ word[index+1:])
"""

"""
# s = "leeetcode"
# s = "aaabaaaa"
# res = []
# i = 0
# while i < len(s):
#     if i < len(s) - 2 and s[i] == s[i+1] == s[i + 2]:
#         res.append(s[i])
#         res.append(s[i+1])
#         i += 3
#     else:
#         res.append(s[i])
#         i += 1
# print("".join(res))


"""
1460 array//https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/description/?envType=problem-list-v2&envId=array
"""
# target = [1,2,3,4]
# arr = [2,4,1,5]
#
# print(sorted(arr) == sorted(target))

"""
https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/description/?envType=problem-list-v2&envId=array
"""
# salary = [4000,3000,1000,2000]
# sorted_ = sorted(salary)
# sorted_.pop(0)
# sorted_.pop(-1)
# print(sum(sorted_) / len(sorted_))

"""
https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/description/?envType=problem-list-v2&envId=sorting
"""
# nums = [-1,10,6,7,-7,1]
# negative_nums = []
# positive_nums = []
# for i in nums:
#     if i < 0:
#         negative_nums.append(i)
#     else:
#         positive_nums.append(i)
#
# for i in sorted(negative_nums):
#     if abs(i) in positive_nums:
#         print(abs(i))
#         break
#     else:
#         print(-1)

"""
https://leetcode.com/problems/decompress-run-length-encoded-list/description/?envType=problem-list-v2&envId=array
"""
# nums = [1,2,3,4]
# res = []
# for i in range(0,len(nums), 2):
#     res.append(nums[i:i +2])
# print(res)
# result = []
# for i in res:
#     result.append([i[1]] * i[0])
# print([n for num in result for n in num ])


"""
https://leetcode.com/problems/merge-similar-items/description/?envType=problem-list-v2&envId=sorting
"""
# items1 = [[1,1],[4,5],[3,8]]
# items2 = [[3,1],[1,5]]
#
# items2.extend(items1)
# d = {}
# print(items2)
# for item in items2:
#     if item[0] not in d:
#         d[item[0]] = item[1]
#     else:
#         d[item[0]] += item[1]
# ret = []
# for key in sorted(d):
#     ret.append([key, d.get(key)])
# print(ret)

"""
https://leetcode.com/problems/license-key-formatting/submissions/1562751749/?envType=problem-list-v2&envId=string
"""
# s = "5F3Z-2e-9-w".split('-')
# k = 4
# s = "".join(s)[::-1].upper()
# print(s)
# res = ''
# for i in range(0,len(s),k):
#     res += s[i:i+k] + '-'
#
# print(res[::-1].lstrip('-'))

"""
https://leetcode.com/problems/repeated-substring-pattern/description/?envType=problem-list-v2&envId=string
"""
# s = "abaaba"
# n = len(s)
# for i in range(1, n // 2 + 1):
#     if n % i == 0:
#         sub = s[:i]
#         if sub * (n // i) == s:
#             print(True)
# print(False)


"""
https://leetcode.com/problems/largest-number/description/?envType=problem-list-v2&envId=sorting
# """
# nums = [3,30,34,5,9]
# nums = list(map(str, nums))
# perms = list(permutations(nums))
# res = []
# for i in perms:
#     res.append("".join(i))
# print(max(res))

"""
https://leetcode.com/problems/check-balanced-string/description/?envType=problem-list-v2&envId=string
"""
# num = "24123"
#
# even = 0
# odd = 0
# for i in range(len(num)):
#     if i % 2 == 0:
#         even += int(num[i])
#     else:
#         odd += int(num[i])
# print(even, '\n', odd)


"""
https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/description/?envType=problem-list-v2&envId=string
"""

# num = "030"
# counter = Counter(num)
# res = ''
# for i in range(len(num)):
#     res+=str(num.count(str(i)))
# print(res == num)

""""
https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case/description/?envType=problem-list-v2&envId=string
"""
# s = "AbCdEfGhIjK"
# res = []
# for i in s:
#     if i.isupper() and i.lower() in s:
#         res.append(i)

# if len(res)==0:
#     print("")
# else:
#     print( max(res))

"""
https://leetcode.com/problems/count-asterisks/description/?envType=problem-list-v2&envId=string
"""
# s ='l|*e*et|c**o|*de|'
# number = 0
# res = 0
# for i in s:
#     if i == '|':
#         number+= 1
#     if i == '*' and number % 2 == 0:
#         res += 1
# print(res)

"""
https://leetcode.com/problems/decode-the-message/description/?envType=problem-list-v2&envId=string
"""
# key = "the quick brown fox jumps over the lazy dog"
# message = "vkbs bs t suepuv"


# letters = string.ascii_lowercase
#
# my_dict = {}
# for i in range(len(key)-1):
#     key = key[i]
#     val = letters[i]
#     if key == " ":
#         my_dict[key] = " "
#     if not key in my_dict:
#         my_dict[key] = val
# print(my_dict)


"""
https://leetcode.com/problems/percentage-of-letter-in-string/?envType=problem-list-v2&envId=string
"""
# s = "sgawtb"
# letter = "s"
# print(floor((s.count(letter)/len(s))*100))

"""
https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/description/?envType=problem-list-v2&envId=string
"""
# number = "1231"
# digit = "1"
# indexes = []
# for i in range(len(number)):
#     if number[i] == digit:
#         indexes.append(i)
# print(indexes)
# nums = []
# for i in indexes:
#     nums.append(number[:i]+number[i+1:])
# print(max(nums))

"""
https://leetcode.com/problems/delete-columns-to-make-sorted/description/?envType=problem-list-v2&envId=string
"""
# count = 0
# strs = ["cba","daf","ghi"]
# for i in list(zip(*strs)):
#     if sorted(i) != list(i):
#         count += 1
# print(count)


"""
https://leetcode.com/problems/first-letter-to-appear-twice/description/?envType=problem-list-v2&envId=string
"""

# s = "abccbaacz"
# my_dict = {}
# for i in range(len(s)):
#     if s[i] not in my_dict:
#         my_dict[s[i]] = [i]
#     else:
#         my_dict[s[i]].append(i)
#
# lists = [val for val in list(my_dict.values()) if len(val) >= 2]
# minn = min(lists, key= lambda x: x[1])
# for key, val in my_dict.items():
#     if val == minn:
#         print(key)

"""
https://leetcode.com/problems/robot-return-to-origin/description/?envType=problem-list-v2&envId=string
"""
# moves = "LL"
#
# move_count = Counter(moves)
# print(move_count)
# if move_count['U'] == move_count['D'] and move_count["L"] == move_count['R']:
#     print(True)
# else:
#     print(False)


"""
https://leetcode.com/problems/find-maximum-number-of-string-pairs/description/?envType=problem-list-v2&envId=string
"""
# words = ["cd","ac","dc","ca","zz"]
# words = ["ff","tx","qr","zw","wr","jr","zt","jk","sq","xx"]
# copied = words.copy()
# count_ = 0
# for i in range(len(words)):
#     if len(set(words[i])) == 1 and words.count(words[i]) != 2:
#         continue
#     else:
#         if words[i][::-1] in words:
#             count_ += 1
#
# print(count_//2)


"""
https://leetcode.com/problems/unique-morse-code-words/description/?envType=problem-list-v2&envId=string
"""

# words = ["gin","zen","gig","msg"]
# dict_ = {'a':".-", 'b':"-...", 'c':"-.-.", 'd':"-..", 'e':".", 'f':"..-.", 'g':"--.", 'h':"....", 'i':"..", 'j':".---",
#          'k':"-.-", 'l':".-..", 'm':"--", 'n':"-.", 'o':"---", 'p':".--.", 'q':"--.-", 'r':".-.", 's':"...", 't':"-",
#          'u':"..-", 'v':"...-", 'w':".--", 'x':"-..-", 'y':"-.--", 'z':"--.."}
# res = []
# tmp = ''
# for word in words:
#     for char in word:
#         tmp += dict_[char]
#     res.append(tmp)
#     tmp = ''
# print(len(set(res)))


"""
https://leetcode.com/problems/find-common-characters/description/?envType=problem-list-v2&envId=string
"""
# words = ["bella","label","roller"]
# count = Counter(words[0])
# result = []
# for i in range(1,len(words)):
#     count &= Counter(words[i])
# for k,v in count.items():
#     result.extend(k*v)
# print(result)


"""
https://leetcode.com/problems/maximum-number-of-balloons/description/
"""
# text = "loonbalxballpoon"
# w = 'balloon'
# print(min(text.count('b'),text.count('a'),text.count('l')//2,text.count('o')//2,text.count('n')))

"""
https://leetcode.com/problems/reverse-integer/description/
"""

# x = -123
# x = str(x).strip('-')
# if x[0] == '-':
#     print(int(x[:1:-1]))
# else:
# print(int(x[::-1]))

"""
https://leetcode.com/problems/score-of-a-string/submissions/1617619134/?envType=problem-list-v2&envId=string
"""
# s = 'hello'
# my_ = []
# for i in range(len(s)-1):
#     res = abs(ord(s[i]) - ord(s[i+1]))
#     my_.append(res)
# print(sum(my_))


# dividend = 10
# divisor = 3
#
# if divisor == 0:
#     raise ValueError("divisor cannot be zero")
# negative = (dividend<0) != (dividend<0)
#
# dividend = abs(dividend)
# divisor = abs(divisor)
# result = 0
#
# while dividend >= divisor:
#     dividend -= divisor
#     result += 1
#
# print(-floor(result )if negative else floor(result))


#https://leetcode.com/problems/longest-common-prefix/

# strs = ["dog","racecar","car"]
# word = min(strs, key=len)
# res = ''
# r = ''
# for i in range(len(word)):
#     for str in strs:
#         if word[i] == str[i]:
#             res += word[i]
#     if len(res) < len(strs):
#         break
#     r +=res[0]
#     res = ''
# print(r)


#https://leetcode.com/problems/excel-sheet-column-number/description/

# letters = string.ascii_uppercase
# dict_ = {}
# for index, val in enumerate(letters):
#     dict_[val] = index+1
#
# res = 0
# columnTitle = "AAA"
# i = len(columnTitle)-1
# for letter in columnTitle:
#     val_letter = dict_[letter]
#     res += val_letter * 26**i
#     i -= 1
# print(res)

# https://leetcode.com/problems/duplicate-zeros/description/
#
# arr = [1,0,2,3,0,4,5,0]
# arr =[0,1,7,6,0,2,0,7]
# arr = [8,5,0,9,0,3,4,7]
# k = len(arr)
# i = 0
# while i <= k-2:
#     if arr[i] == 0:
#         arr.insert(i+1, 0)
#         i += 2
#     else:
#         i += 1
# print(arr[:k])

#  in leetcode : arr[:] = arr[:k] in place change: in one memory location


# https://leetcode.com/problems/find-the-town-judge/description/

# n = 4
# trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
# n = 3
# trust = [[1,3],[2,3],[3,1]]
# if n == 1:
#     print(n)
# elif n==2 and len(trust) == 0:
#     print(-1)
# else:
#     list_ = [t[0] for t in trust]
#     judge =[t[1] for t in trust]
#     count_ =Counter(judge)
#     judge_most_voices = max(count_, key=count_.get)
#     num_of_voices = count_.get(judge_most_voices)
#
#     if num_of_voices == n-1 and judge_most_voices not in list_:
#         print(judge_most_voices)
#     else:
#         print(-1)



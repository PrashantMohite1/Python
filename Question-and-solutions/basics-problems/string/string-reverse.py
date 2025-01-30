
"""
Q

Given a string s, reverse the string without reversing its individual words. Words are separated by spaces.

Note: The string may contain leading or trailing spaces, or multiple spaces between two words. The returned string should only have a single space separating the words, and no extra spaces should be included.

Examples :

Input: s = " i like this program very much "
Output: "much very program this like i"
Explanation: After removing extra spaces and reversing the whole string (not individual words), the input string becomes "much very program this like i". 


"""



s = "I like the Program Very Much"

rev = s.split()
rev2 = " ".join(rev[::-1])
print(rev2)



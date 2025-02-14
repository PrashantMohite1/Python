"""Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring."""


s = "pwwkew"


def lengthOfLongestSubstring(s: str) -> int:
    # Create a set to store unique characters in the current window
    char_set = set()
    
    # Initialize two pointers: start and end
    start = 0
    max_length = 0
    
    # Iterate over the string using 'end' as the pointer for the right end of the window
    for end in range(len(s)):
        # If the character at 'end' is in the set, we have a duplicate
        while s[end] in char_set:
            # Remove the character at 'start' from the set and move start forward
            char_set.remove(s[start])
            start += 1
        
        # Add the current character to the set
        char_set.add(s[end])
        
        # Update the maximum length of the window (substring without repeating characters)
        max_length = max(max_length, end - start + 1)
    
    return max_length

"""
Big solution guy here.
"""

def lengthOfLongestSubstring(s: str) -> int:
    
    past_chars = {}
    longest_substr = 0
    unique_streak = 0

    for index in range(len(s)):

        try: #character has already been seen
            last_index = past_chars[s[index]]
            len_since_last = index - last_index
            unique_streak += 1

            if len_since_last < unique_streak:
                unique_streak = len_since_last

            if unique_streak > longest_substr:
                longest_substr = unique_streak

            past_chars[s[index]] = index #update dictionary

        except KeyError: #character has not been seen
            past_chars[s[index]] = index #add to dictionary
            unique_streak += 1
            
            if unique_streak > longest_substr:
                longest_substr = unique_streak
    
    return longest_substr

test_str = "abba"
print(f" longest sub-string length: {lengthOfLongestSubstring(test_str)}")

test_str_2 = "tmmzuxt"
print(f"str: {test_str_2} unique len: {lengthOfLongestSubstring(test_str_2)}")
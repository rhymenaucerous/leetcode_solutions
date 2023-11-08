# Solution #1

def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    my_str = str(x)
    my_str_len = len(my_str)
    half = my_str_len//2

    if my_str_len%2 == 0:
        second_half = half - 1
    else:
        second_half = half
    
    print(f"first half: {my_str[:half]}, second_half:{my_str[my_str_len:second_half:-1]}")

    if my_str[:half] == my_str[my_str_len:second_half:-1]:
        return True
    else:
        return False

print(isPalindrome(1234))
print(isPalindrome(12221))
print(isPalindrome(9888897))

def isPalindrome(self, x: int) -> bool:
    if x < 0:
        return False
    
    original = x
    reversed = 0
    
    while x != 0:
        digit = x%10
        reversed = reversed * 10 + digit
        x = x//10
    
    if reversed == original:
        return True
    else:
        return False
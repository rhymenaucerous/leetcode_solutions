# better solution

def roman_to_int_sol1 (s: str) -> int:
    """
    solution 1.
    """

    str_len = len(s)

    if str_len == 0:
        return 0

    ans = 0

    conversions = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    }

    for index in range(str_len):
        if (index + 1) < str_len and conversions[s[index]] < conversions[s[index + 1]]:
            ans -= conversions[s[index]]
        else:
            ans += conversions[s[index]]

    return ans

# Original solution

def roman_to_int_sol2 (s: str) -> int:
    """
    solution 2.
    """

    str_len = len(s)

    if str_len == 0:
        return 0

    ans = 0
    skip = 0

    for index in range(str_len):

        if skip == 1:
            skip = 0
            continue

        if s[index] == 'I':
            if index == str_len - 1:
                ans += 1
                continue

            if s[index + 1] == 'V':
                ans += 4
                skip = 1
            elif s[index + 1] == 'X':
                ans += 9
                skip = 1
            else:
                ans += 1

        elif s[index] == 'V':
            ans += 5

        elif s[index] == 'X':
            if index == str_len - 1:
                ans += 10
                continue

            if s[index + 1] == 'L':
                ans += 40
                skip = 1
            elif s[index + 1] == 'C':
                ans += 90
                skip = 1
            else:
                ans += 10

        elif s[index] == 'L':
            ans += 50

        elif s[index] == 'C':
            if index == str_len - 1:
                ans += 100
                continue

            if s[index + 1] == 'D':
                ans += 400
                skip = 1
            elif s[index + 1] == 'M':
                ans += 900
                skip = 1
            else:
                ans += 100

        elif s[index] == 'D':
            ans += 500

        elif s[index] == 'M':
            ans += 1000

        else:
            print("invalid packet recieved")
            return -1

    return ans

# End of file

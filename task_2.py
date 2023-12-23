from collections import deque  


def is_palindrome(data :str):
    word = str(data).lower().replace(' ', '')
    d = deque(word)
    while len(d) > len(d) % 2:
        if d.pop() != d.popleft():
            return f"{data} is not palindrome"
        else:
            continue
    return f"{data} is palindrome"


if __name__ == "__main__":
    print(is_palindrome("kottok"))
    print(is_palindrome("kotctok"))
    print(is_palindrome("kotcTok"))
    print(is_palindrome("ko tc Tok"))
    print(is_palindrome("ko tc ok"))
        
def is_palindrome(s):
    return s == s[::-1]
word = input("Enter a word: ")
if is_palindrome (word):
    print(f"{word} is a palindrome")
    print("DHRUV GUPTA, 2024UCI8045")
else:
    print(f"{word} is not a palindrome")
    print("DHRUV GUPTA, 2024UCI8045")

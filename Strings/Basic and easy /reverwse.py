def reverseWords(s):

    i = len(s) - 1
    ans = ""

    while i >= 0:

        # Skip spaces
        while i >= 0 and s[i] == " ":
            i -= 1

        # If reached beginning
        if i < 0:
            break

        # Mark end of word
        j = i

        # Move till beginning of word
        while i >= 0 and s[i] != " ":
            i -= 1

        # Extract word
        word = s[i + 1:j + 1]

        # Add to answer
        if ans == "":
            ans += word
        else:
            ans += " " + word

    return ans
s = "the sky is blue"
print(reverseWords(s))
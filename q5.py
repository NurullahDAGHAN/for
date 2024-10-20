string1 = "aabbcsdw"
string2 = "abbbcsdd"

for i in range(len(string2)):
    char1 = string2[i]
    char2 = string1[i]

    if char1 == char2:
        print(char1)
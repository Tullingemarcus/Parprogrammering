def censor(word):
    censor = ""
    for letter in word:
        if letter in "AOUIYÅÄÖEaouiyeåäö":
            censor += "*"
        else:
            censor += letter

    return censor

print(censor(input("word? ")))
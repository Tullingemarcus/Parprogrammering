
def rearrange_dif():
    lowest = ""
    highest = ""
    list_dif = []

    number = str(input(""))

    for position in range(len(number)):
        list_dif.append(number[position])

    list_dif.sort()
    for digit in list_dif:
        lowest += str(digit)
    
    list_dif.sort(reverse=True)
    for digit in list_dif:
        highest += str(digit)

    anwser = int(highest)-int(lowest)
    return anwser



print(rearrange_dif())
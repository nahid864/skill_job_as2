def first_and_last(str):
    str=str(input())
    if len(str)<2:
        return ''
    return str[0:2] + str[-2:]
print(first_and_last(str))
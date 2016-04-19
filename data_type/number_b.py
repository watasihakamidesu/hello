def test(number):
    if number > 1:
        return format(number, 'b').count('1')
    elif number == 0:
        return 0
    else:
        return format(number, '1<33b').count('1')

print test(39)
print test(-1)
print test(0)

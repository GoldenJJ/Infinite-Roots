def squareroot(root, num, cycles=1000000, precision=0.000000000001):
    guess = num / root
    i = 1
    cycle = 0
    while cycle < cycles and guess ** root != num and abs((guess ** root) - num) > precision:

        error = guess ** root - num  # greater than 0 if square is greater than num

        if error > 0:
            if guess > 0:
                guess = guess - num / (root * i)
            else:
                guess = guess + num / (root * i)
        elif error == 0:
            return guess
        else:
            guess = guess + num / (root * i)

        if int(guess) ** 2 == num:
            return float(int(guess))

        i += 0.5
        cycle += 1
    return guess


num = int(input("Number to root: "))
root = int(input("Degree of root: "))

print(f"Root {root} of {num}: {squareroot(root, num)}")

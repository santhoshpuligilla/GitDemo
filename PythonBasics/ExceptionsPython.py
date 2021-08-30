ItemsInCart = 0

if ItemsInCart != 2:
    pass
assert (ItemsInCart == 0)

# try, catch

try:
    with open('filelog.txt', 'r') as reader:
        reader.read()

except:
    print("Some how I reached this block because there is failure in try block")



try:
    with open('filelog.txt', 'r') as reader:
        reader.read()

except Exception as e:
    print(e)

finally:
    print("cleaning up records")
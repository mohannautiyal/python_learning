# A generator is a special type of function that produces
# one value at a time
# on demand rather than returning all values at once

# Generator uses the yield keyword to return a value and saves its state
# i.e generator remembers where it left between successive calls,
# making it memory efficient

# Only the current value (and its state) is kept in memory, not the whole
# list of values
# Returns a generator object, which can be iterated using for loop or next()


def mygenerator():
    yield   2
    yield 4
    yield 6

mygen = mygenerator()

print(next(mygen))
print(next(mygen))
print(next(mygen))

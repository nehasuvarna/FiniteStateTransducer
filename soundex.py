from fst import FST
import string, sys
from fsmutils import composechars, trace

def letters_to_numbers():
    """
    Returns an FST that converts letters to numbers as specified by
    the soundex algorithm
    """

    # Let's define our first FST
    f1 = FST('soundex-generate')

    # Indicate that '1' is the initial state
    f1.add_state('start')
    f1.add_state('0')
    f1.add_state('1')
    f1.add_state('2')
    f1.add_state('3')
    f1.add_state('4')
    f1.add_state('5')
    f1.add_state('6')
    f1.initial_state = 'start'

    # Set all the final states
    f1.set_final('0')
    f1.set_final('1')
    f1.set_final('2')
    f1.set_final('3')
    f1.set_final('4')
    f1.set_final('5')
    f1.set_final('6')

    # Add the rest of the arcs
    for letter in string.ascii_lowercase:

        if letter in ['a', 'e', 'i', 'o', 'u', 'h', 'w', 'y']:
            f1.add_arc('start', '0', (letter), (letter))
            f1.add_arc('0', '0', (letter), ())
            f1.add_arc('1', '0', (letter), ())
            f1.add_arc('2', '0', (letter), ())
            f1.add_arc('3', '0', (letter), ())
            f1.add_arc('4', '0', (letter), ())
            f1.add_arc('5', '0', (letter), ())
            f1.add_arc('6', '0', (letter), ())

        elif letter in ['b', 'f', 'p', 'v']:
            f1.add_arc('start', '1', (letter), (letter))
            f1.add_arc('1', '1', (letter), ())
            f1.add_arc('0', '1', (letter), ('1'))
            f1.add_arc('2', '1', (letter), ('1'))
            f1.add_arc('3', '1', (letter), ('1'))
            f1.add_arc('4', '1', (letter), ('1'))
            f1.add_arc('5', '1', (letter), ('1'))
            f1.add_arc('6', '1', (letter), ('1'))

        elif letter in ['c', 'g', 'j', 'k', 'q', 'x', 'z', 's']:
            f1.add_arc('start', '2', (letter), (letter))
            f1.add_arc('2', '2', (letter), ())
            f1.add_arc('1', '2', (letter), ('2'))
            f1.add_arc('0', '2', (letter), ('2'))
            f1.add_arc('3', '2', (letter), ('2'))
            f1.add_arc('4', '2', (letter), ('2'))
            f1.add_arc('5', '2', (letter), ('2'))
            f1.add_arc('6', '2', (letter), ('2'))

        elif letter in ['d', 't']:
            f1.add_arc('start', '3', (letter), (letter))
            f1.add_arc('3', '3', (letter), ())
            f1.add_arc('1', '3', (letter), ('3'))
            f1.add_arc('2', '3', (letter), ('3'))
            f1.add_arc('0', '3', (letter), ('3'))
            f1.add_arc('4', '3', (letter), ('3'))
            f1.add_arc('5', '3', (letter), ('3'))
            f1.add_arc('6', '3', (letter), ('3'))

        elif letter in ['l']:
            f1.add_arc('start', '4', (letter), (letter))
            f1.add_arc('4', '4', (letter), ())
            f1.add_arc('1', '4', (letter), ('4'))
            f1.add_arc('2', '4', (letter), ('4'))
            f1.add_arc('3', '4', (letter), ('4'))
            f1.add_arc('0', '4', (letter), ('4'))
            f1.add_arc('5', '4', (letter), ('4'))
            f1.add_arc('6', '4', (letter), ('4'))

        elif letter in ['m', 'n']:
            f1.add_arc('start', '5', (letter), (letter))
            f1.add_arc('5', '5', (letter), ())
            f1.add_arc('1', '5', (letter), ('5'))
            f1.add_arc('2', '5', (letter), ('5'))
            f1.add_arc('3', '5', (letter), ('5'))
            f1.add_arc('4', '5', (letter), ('5'))
            f1.add_arc('0', '5', (letter), ('5'))
            f1.add_arc('6', '5', (letter), ('5'))

        else:
            f1.add_arc('start', '6', (letter), (letter))
            f1.add_arc('6', '6', (letter), ())
            f1.add_arc('1', '6', (letter), ('6'))
            f1.add_arc('2', '6', (letter), ('6'))
            f1.add_arc('3', '6', (letter), ('6'))
            f1.add_arc('4', '6', (letter), ('6'))
            f1.add_arc('5', '6', (letter), ('6'))
            f1.add_arc('0', '6', (letter), ('6'))

        # else:
        #     f1.add_arc('next', 'next', (letter), ())
    return f1

    # The stub code above converts all letters except the first into '0'.
    # How can you change it to do the right conversion?

def truncate_to_three_digits():
    """
    Create an FST that will truncate a soundex string to three digits
    """

    # Ok so now let's do the second FST, the one that will truncate
    # the number of digits to 3
    f2 = FST('soundex-truncate')

    # Indicate initial and final states
    f2.add_state('1')
    f2.add_state('2')
    f2.add_state('3')
    f2.add_state('4')
    f2.add_state('5')
    f2.initial_state = '1'
    f2.set_final('2')
    f2.set_final('3')
    f2.set_final('4')
    f2.set_final('5')

    # Add the arcs
    for letter in string.letters:
        f2.add_arc('1', '2', (letter), (letter))

    for n in range(10):
        f2.add_arc('1', '3', (str(n)), (str(n)))
        f2.add_arc('2', '3', (str(n)), (str(n)))
        f2.add_arc('3', '4', (str(n)), (str(n)))
        f2.add_arc('4', '5', (str(n)), (str(n)))
        f2.add_arc('5', '5', (str(n)), ())
    return f2

    # The above stub code doesn't do any truncating at all -- it passes letter and number input through
    # what changes would make it truncate digits to 3?

def add_zero_padding():
    # Now, the third fst - the zero-padding fst
    f3 = FST('soundex-padzero')

    f3.add_state('1')
    f3.add_state('1a')
    f3.add_state('1b')
    f3.add_state('2')
    
    f3.initial_state = '1'
    f3.set_final('2')

    for letter in string.letters:
        f3.add_arc('1', '1', (letter), (letter))

    f3.add_arc('1', '1a', (), ('0'))
    f3.add_arc('1a', '1b', (), ('0'))
    f3.add_arc('1b', '2', (), ('0'))

    for number in xrange(10):
        f3.add_arc('1', '1a', (str(number)), (str(number)))
        f3.add_arc('1a', '1b', (str(number)), (str(number)))
        f3.add_arc('1b', '2', (str(number)), (str(number)))


    return f3

    # The above code adds zeroes but doesn't have any padding logic. Add some!

if __name__ == '__main__':
    user_input = raw_input().strip()
    f1 = letters_to_numbers()
    f2 = truncate_to_three_digits()
    f3 = add_zero_padding()

    if user_input:
        print("%s -> %s" % (user_input, composechars(tuple(user_input), f1)))

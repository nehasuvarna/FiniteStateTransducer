import sys
from fst import FST
from fsmutils import composewords

kFRENCH_TRANS = {0: "zero", 1: "un", 2: "deux", 3: "trois", 4:
                 "quatre", 5: "cinq", 6: "six", 7: "sept", 8: "huit",
                 9: "neuf", 10: "dix", 11: "onze", 12: "douze", 13:
                 "treize", 14: "quatorze", 15: "quinze", 16: "seize",
                 20: "vingt", 30: "trente", 40: "quarante", 50:
                 "cinquante", 60: "soixante", 100: "cent"}

kFRENCH_AND = 'et'

def prepare_input(integer):
    assert isinstance(integer, int) and integer < 1000 and integer >= 0, \
      "Integer out of bounds"
    return list("%03i" % integer)

def french_count():
    f = FST('french')

    f.add_state('start')

    f.add_state('0xx')
    f.add_state('nxx')

    f.add_state('00x')

    f.add_state('n0x')
    f.add_state('n1x')
    f.add_state('nnx')
    f.add_state('n7x')
    f.add_state('n8x')
    f.add_state('n9x')
    f.add_state('last')

    f.initial_state = 'start'
    f.set_final('last')

    for ii in xrange(10):
        f.add_arc('00x', 'last', [str(ii)], [kFRENCH_TRANS[ii]])
        if ii == 0:
             f.add_arc('start', '0xx', [str(ii)], ())
             f.add_arc('0xx', '00x', [str(ii)], ())
             f.add_arc('nxx', 'n0x', [str(ii)], ())
             f.add_arc('n0x', 'last', [str(ii)], ())
             f.add_arc('n1x', 'last', [str(ii)], [kFRENCH_TRANS[ii + 10]])
             f.add_arc('nnx', 'last', [str(ii)], ())
             f.add_arc('n7x', 'last', [str(ii)], [kFRENCH_TRANS[ii+10]])
             f.add_arc('n8x', 'last', [str(ii)], ())
             f.add_arc('n9x', 'last', [str(ii)], [kFRENCH_TRANS[ii+10]])

        if ii == 1:
            f.add_arc('start', 'nxx', [str(ii)], [kFRENCH_TRANS[100]])
            f.add_arc('0xx', 'n1x', [str(ii)], ())
            f.add_arc('nxx', 'n1x', [str(ii)], ())
            f.add_arc('n0x', 'last', [str(ii)], [kFRENCH_TRANS[ii]])
            f.add_arc('n1x', 'last', [str(ii)], [kFRENCH_TRANS[ii + 10]])
            f.add_arc('nnx', 'last', [str(ii)], [kFRENCH_AND,kFRENCH_TRANS[ii]])
            f.add_arc('n7x', 'last', [str(ii)], [kFRENCH_AND,kFRENCH_TRANS[ii+10]])
            f.add_arc('n8x', 'last', [str(ii)], [kFRENCH_TRANS[ii]])
            f.add_arc('n9x', 'last', [str(ii)], [kFRENCH_TRANS[ii+10]])

        if ii in range(2,7):
            f.add_arc('start', 'nxx', [str(ii)], [kFRENCH_TRANS[ii],kFRENCH_TRANS[100]])
            f.add_arc('0xx', 'nnx', [str(ii)], [kFRENCH_TRANS[ii * 10]])
            f.add_arc('nxx', 'nnx', [str(ii)], [kFRENCH_TRANS[ii * 10]])
            f.add_arc('n0x', 'last', [str(ii)], [kFRENCH_TRANS[ii]])
            f.add_arc('n1x', 'last', [str(ii)], [kFRENCH_TRANS[ii + 10]])
            f.add_arc('nnx', 'last', [str(ii)], [kFRENCH_TRANS[ii]])
            f.add_arc('n7x', 'last', [str(ii)], [kFRENCH_TRANS[ii+10]])
            f.add_arc('n8x', 'last', [str(ii)], [kFRENCH_TRANS[ii]])
            f.add_arc('n9x', 'last', [str(ii)], [kFRENCH_TRANS[ii + 10]])

        if ii == 7:
            f.add_arc('start', 'nxx', [str(ii)], [kFRENCH_TRANS[ii],kFRENCH_TRANS[100]])
            f.add_arc('0xx', 'n7x', [str(ii)], [kFRENCH_TRANS[6 * 10]])
            f.add_arc('nxx', 'n7x', [str(ii)], [kFRENCH_TRANS[6*10]])
            f.add_arc('n0x', 'last', [str(ii)], [kFRENCH_TRANS[ii]])
            f.add_arc('n1x', 'last', [str(ii)],  [kFRENCH_TRANS[10], kFRENCH_TRANS[ii]])
            f.add_arc('nnx', 'last', [str(ii)], [kFRENCH_TRANS[ii]])
            f.add_arc('n7x', 'last', [str(ii)], [kFRENCH_TRANS[10], kFRENCH_TRANS[ii]])
            f.add_arc('n8x', 'last', [str(ii)], [kFRENCH_TRANS[ii]])
            f.add_arc('n9x', 'last', [str(ii)], [kFRENCH_TRANS[10], kFRENCH_TRANS[ii]])

        if ii == 8:
            f.add_arc('start', 'nxx', [str(ii)], [kFRENCH_TRANS[ii],kFRENCH_TRANS[100]])
            f.add_arc('0xx', 'n8x', [str(ii)], [kFRENCH_TRANS[4], kFRENCH_TRANS[20]])
            f.add_arc('nxx', 'n8x', [str(ii)], [kFRENCH_TRANS[4], kFRENCH_TRANS[20]])
            f.add_arc('n0x', 'last', [str(ii)], [kFRENCH_TRANS[ii]])
            f.add_arc('n1x', 'last', [str(ii)],  [kFRENCH_TRANS[10], kFRENCH_TRANS[ii]])
            f.add_arc('nnx', 'last', [str(ii)], [kFRENCH_TRANS[ii]])
            f.add_arc('n7x', 'last', [str(ii)], [kFRENCH_TRANS[10], kFRENCH_TRANS[ii]])
            f.add_arc('n8x', 'last', [str(ii)], [kFRENCH_TRANS[ii]])
            f.add_arc('n9x', 'last', [str(ii)], [kFRENCH_TRANS[10], kFRENCH_TRANS[ii]])

        if ii == 9:
            f.add_arc('start', 'nxx', [str(ii)], [kFRENCH_TRANS[ii],kFRENCH_TRANS[100]])
            f.add_arc('0xx', 'n9x', [str(ii)], [kFRENCH_TRANS[4], kFRENCH_TRANS[20]])
            f.add_arc('nxx', 'n9x', [str(ii)], [kFRENCH_TRANS[4], kFRENCH_TRANS[20]])
            f.add_arc('n0x', 'last', [str(ii)], [kFRENCH_TRANS[ii]])
            f.add_arc('n1x', 'last', [str(ii)],  [kFRENCH_TRANS[10], kFRENCH_TRANS[ii]])
            f.add_arc('nnx', 'last', [str(ii)], [kFRENCH_TRANS[ii]])
            f.add_arc('n7x', 'last', [str(ii)], [kFRENCH_TRANS[10], kFRENCH_TRANS[ii]])
            f.add_arc('n8x', 'last', [str(ii)], [kFRENCH_TRANS[ii]])
            f.add_arc('n9x', 'last', [str(ii)], [kFRENCH_TRANS[10], kFRENCH_TRANS[ii]])
    return f


if __name__ == '__main__':
    f = french_count()
    string_input = raw_input()
    user_input = int(string_input)
    if string_input:
        print user_input, '-->',
        print " ".join(f.transduce(prepare_input(user_input)))
    #
    # f1 = open("out.txt", "w")
    # for num in range(0,1000):
    #     print num
    #     f1.write(repr(num))
    #     f1.write(":")
    #     f1.write(" ".join(f.transduce(prepare_input(num))))
    #     f1.write("\n")
    # f1.close()
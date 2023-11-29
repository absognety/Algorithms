# Input = ['a','b','c'], fillvalue = '*', offset = 1
# Output = [('a', '*'), ('b', 'a'), ('c', 'b'), ('*', 'c')]

def pairwise_offset(sequence, fillvalue, offset):
    if offset == 0:
        output = zip(sequence,sequence)
        return list(output)
    sequence2 = sequence1 = sequence.copy()
    for i in range(offset):
        sequence1 = sequence1 + [fillvalue]
        sequence2 = [fillvalue] + sequence2
    return list(zip(sequence1,sequence2))

if __name__ == '__main__':
    # sequence = input().strip().split(",")
    sequence = ['a','b','c']
    # _fillvalue = input()
    _fillvalue = '*'
    _offset = '1'
    try:
        _offset = int(input())
        assert _offset >= 0, "Given offset is negative"
    except Exception as e:
        print (str(e))
        print ("Unsupported value of offset passed, expected int given {} with value {}"\
               .format(type(_offset),_offset))
        print ("Setting offset to default value 0")
        _offset = 0
    print (pairwise_offset(sequence=sequence,fillvalue=_fillvalue,
                           offset=_offset))
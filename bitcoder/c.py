__author__ = 'Joe'


def export(field_desc):
    """

    :param field_desc:
    :type field_desc: bitcoder.bitcoder.Encoded
    :return:
    """
    output = '// Automatically generated file, changes may be lost when file is regenerated\n'
    output += '\n'
    output += 'struct {}\n'.format(field_desc.__class__.__name__)
    output += '{\n'

    bit = 0
    reserved_count = 0
    for name, field in field_desc.fields().iteritems():
        # padding
        if field.start != bit:
            output += '\tunsigned int {}: {}\n'.format('reserved_'+str(reserved_count), field.length)
            reserved_count += 1

        # add field
        output += '\tunsigned int {}: {}\n'.format(name, field.length)
        bit = field.start+field.length

    output += '} pack;\n'
    return output

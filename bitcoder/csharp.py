__author__ = 'Joe'


def export(field_desc):
    """

    :param field_desc:
    :type field_desc: bitcoder.bitcoder.Encoded
    :return:
    """
    output = '// Automatically generated file, changes may be lost when file is regenerated\n'
    output += '\n'
    for name, field in field_desc.fields().iteritems():
        output += 'public const int {}_mask = {};\n'.format(name, 1**field.length << field.start)
        output += 'public const int {}_start = {};\n'.format(name, field.start)

    return output

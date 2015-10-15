import json

__author__ = 'Joe'


def export(field_desc):
    """

    :param field_desc:
    :type field_desc: bitcoder.bitcoder.Encoded
    :return:
    """
    output = {}
    for name, field in field_desc.fields().iteritems():
        output[name] = {
            'mask': 1**field.length << field.start,
            'start': field.start,
        }

    output = {field_desc.__class__.__name__: output}
    return json.dumps(output, sort_keys=True, indent=2)

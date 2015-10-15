from collections import OrderedDict

__author__ = 'Joe'


class DescriptorAccessMixin:
    def _list_instances(self, *targets):
        rtn = {}
        for name, field in self.__class__.__dict__.items():
            if isinstance(field, targets):
                rtn[name] = field
        return rtn


class Field(object):
    def __init__(self, start, length):
        self._start = start
        self._len = length

    def __str__(self):
        return 'Field:' + ','.join(map(str, xrange(self._start, self._start+self._len)))

    @property
    def start(self):
        return self._start

    @property
    def length(self):
        return self._len


class Bool(Field):
    def __init__(self, start):
        super(Bool, self).__init__(start, 1)


class Encoded(DescriptorAccessMixin):
    bits = None

    def fields(self):
        items = dict((x, getattr(self, x)) for x in self._list_instances(Field))
        return OrderedDict(sorted(items.items(), key=lambda x: x[1].start))

    def __str__(self):
        formatter = '{}:\t{}\n'
        desc = ''
        bit = 0
        for name, field in self.fields().iteritems():
            for x in xrange(bit, field.start):
                desc += formatter.format(bit, 'Reserved')
                bit += 1
            for x in xrange(bit, bit+field.length):
                desc += formatter.format(bit, name)
                bit += 1
        for x in xrange(bit, self.bits):
            desc += formatter.format(bit, 'Reserved')
            bit += 1
        return desc

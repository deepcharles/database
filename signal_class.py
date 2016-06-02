# Details of the implementation:
# http://docs.scipy.org/doc/numpy-1.10.1/user/basics.subclassing.html

import numpy as np


class Signal(np.ndarray):

    def __new__(cls, input_array, **kwargs):
        # Input array is an already formed ndarray instance
        # We first cast to be our class type
        obj = np.asarray(input_array).view(cls)
        # add the new attribute to the created instance

        # we keep a list of the attributes somewhere.
        obj._meta = list(kwargs.keys())

        for k, v in kwargs.items():
            setattr(obj, k, v)
        # Finally, we must return the newly created object:
        return obj

    def __array_finalize__(self, obj):
        # ``self`` is a new object resulting from
        # ndarray.__new__(Signal, ...), therefore iat only has
        # attributes that the ndarray.__new__ constructor gave it -
        # i.e. those of a standard ndarray.
        #
        # We could have got to the ndarray.__new__ call in 3 ways:
        # From an explicit constructor - e.g. Signal():
        #    obj is None
        #    (we're in the middle of the Signal.__new__
        #    constructor, and self.info will be set when we return to
        #    Signal.__new__)
        if obj is None:
            return
        # From view casting - e.g arr.view(Signal):
        #    obj is arr
        #    (type(obj) can be Signal)
        # From new-from-template - e.g infoarr[:3]
        #    type(obj) is Signal
        #
        # Note that it is here, rather than in the __new__ method,
        # that we set the default value for 'info', because this
        # method sees all creation of default objects - with the
        # Signal.__new__ constructor, but also with
        # arr.view(Signal).
        self._meta = getattr(obj, "_meta", None)
        if self._meta is not None:
            for key in getattr(obj, "_meta", None):
                setattr(self, key, getattr(obj, key, None))
        # We do not need to return anything

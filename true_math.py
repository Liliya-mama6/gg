import inspect
import pprint


def introspection_info(obj):
    return {
        'type': type(obj).__name__,
        'attributes': obj.__dir__,
        'methods': dir(obj),
        'module': inspect.getmodule(obj, 'sirius1.py')
    }


pprint.pprint(introspection_info(111))

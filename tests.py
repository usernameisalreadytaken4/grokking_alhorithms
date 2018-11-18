a = {
   'b' : 4,
   'c' : {
      'd': 3,
      'e': 5,
       'c': {
           'd': 6
       }
    }
}

b = {
    'b': 4,
    'c.d': 3,
    'c.e': 5,
    'c.c.d': 6
}

new = {}


def get_inside(_dict, _key):
    for key in _dict.keys():
        if isinstance(_dict[key], dict):
            temp_key = key
            if _key:
                temp_key = _key + '.' + key
            _dict[key] = get_inside(_dict[key], temp_key)
        else:
            if _key:
                new[_key + '.' + key] = _dict[key]
            else:
                new[key] = _dict[key]

get_inside(a, None)

print(new)
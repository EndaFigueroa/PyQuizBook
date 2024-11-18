def create_dict_from_lists(keys, values):
    answer = dict(zip(keys,values))
    return answer
    # """
    # This function returns a dict made from two lists.
    # """
    # pass  # implement me

def merge_two_dicts(d1, d2):
    answer = d1
    d1.update(d2)
    return answer
    # """
    # Merge two Python dictionaries into one
    # """
    # pass  # implement me

def init_dict_with_values(lst, d1):
    answer = {}
    for i in lst:
        answer[i]=d1
    return answer
    # """
    # Create a dict with default values for each key listed.

    # """
    # #
    # pass  # implement me

def extract_keys_to_dict(datadict, keylist):
    answer = {}
    for i in keylist:
        answer[i] = datadict[i]
    return answer
    # """
    # Create a dictionary by extracting the keylist from a given dictionary
    # """
    # #
    # pass  # implement me

def delete_keys_from_dict(datadict, keylist):
    for i in keylist:
        del datadict[i]
    return datadict
    # """
    # Delete a list of keys from a dictionary
    # """
    # pass

def check_dict_for_key(datadict, key):
    answer=datadict.values()
    if key in answer:
        return True
    return False
    # """
    # Check if a value exists in a dictionary
    # (NO FOR loops!)
    # """
    # pass

def get_key_of_min_value(ddd):
    littleGuy = ddd.values()
    littleGuy = min(littleGuy)
    dddKeys = ddd.keys()

    for i in dddKeys:
        if ddd[i] == littleGuy:
            return i
    # """
    # Get the key of the minimum value from a dictionary
    # """
    # pass

def get_key_of_max_value(ddd):
    littleGuy = ddd.values()
    littleGuy = max(littleGuy)
    dddKeys = ddd.keys()

    for i in dddKeys:
        if ddd[i] == littleGuy:
            return i
    # """
    # Get the key of the maximum value from a dictionary
    # """
    # pass
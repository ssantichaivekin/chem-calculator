import csv

def write_dict(destination, dict_array, order) :
    '''
    Write an array of dictionary to a csv file.
    dict_array = [{'a':1, 'b':2}, {'a':3, 'b':4}]
    order = ['b', 'a']
    File :
    2,1
    4,3
    '''
    with open(destination, 'w') as f :
        for elem in dict_array :
            writer = csv.DictWriter(f, fieldnames=order)
            writer.writerow(elem)

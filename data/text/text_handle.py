import cPickle as pickle

def write(name, data):
    with open(name, 'wb') as f:
        pickle.dump(data, f)

def read(name):
    with open(name, 'rb') as f:
        return pickle.load(f)


if __name__ == '__main__':
    write("hello", {"hello":"world","jhchen":"asdasd","aaaa":[1,2,3,4]})
    print read("hello")
    #print data

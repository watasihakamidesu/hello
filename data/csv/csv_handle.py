import csv

def read(name):
    reader = csv.reader(file(name, 'rb'))
    for line in reader:
        print line


def write(name,data):
    writer = csv.writer(open(name, 'w'))
    writer.writerow()
    lines = [range(3) for i in range(5)]
    for line in lines:
        writer.writerow(line)

if __name__ == '__main__':
    read('your.csv')
    write('your.csv',['Column1', 'Column2', 'Column3'])

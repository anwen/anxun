
def random_sayings():
    file1 = 'utils/sayings.txt'
    a = []
    with open(file1) as f:
        for eachline in f:
            a.append(str(eachline.replace('\n', '')))
    import random
    return random.choice(a)

if __name__ == '__main__':
    print(random_sayings())

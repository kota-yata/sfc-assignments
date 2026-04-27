def read_items_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f.readlines()]

def process_items(data):
    total = 0
    for item in data:
        total += int(item)
    average = total / len(data)
    return average

if __name__ == "__main__":
    items = read_items_from_file('items.txt')
    print(process_items(items))

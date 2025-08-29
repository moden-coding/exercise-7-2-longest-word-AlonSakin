def longest(list : list):
    largest = ""
    for string in list:
        if len(string) > len(largest):
            largest = string
    return largest

if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))
# python3

def build_heap(data):
    swaps = []
    n = len(data)
    for i in range(len(data) // 2, -1, -1):
        sift_down(i, data, swaps)
    return swaps


def build_heap(data):
    swaps = []
    n = len(data)
    for i in range(len(data) // 2, -1, -1):
        sift_down(i, data, swaps)
    return swaps


def sift_down(i, data, swaps):
    n = len(data)
    max_index = i
    l = 2 * i + 1
    if l < n and data[l] < data[max_index]:
        max_index = l
    r = 2 * i + 2
    if r < n and data[r] < data[max_index]:
        max_index = r
    if i != max_index:
        data[i], data[max_index] = data[max_index], data[i]
        swaps.append((i, max_index))
        sift_down(max_index, data, swaps)


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n
    swaps = build_heap(data)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)

        
if __name__ == "__main__":
    main()



def main():
    try:
        n = int(input())
    except ValueError:
        print('')
        return
    
    data = list(map(int, input().split()))

    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()




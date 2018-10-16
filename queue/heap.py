
class Heap:
    def __init__(self, data_list):
        if data_list is None:
            raise ValueError('data_list is invalid')
        self.data_list = data_list

    def max_heapify(self, index, heap_size):
        """recursively build a MAX-heap"""
        i_max = index
        i_left = 2 * index + 1
        i_right = 2 * index + 2

        if i_left < heap_size and \
                self.data_list[i_left] > self.data_list[index]:
            i_max = i_left
        if i_right < heap_size and \
                self.data_list[i_right] > self.data_list[i_max]:
            i_max = i_right

        if i_max != index:
            self.data_list[i_max], self.data_list[index] = \
                self.data_list[index], self.data_list[i_max]
            self.max_heapify(i_max, heap_size)

    def min_heapify(self, index, heap_size):
        """iteratively build a MIN-heap"""
        while True:
            i_max = index
            i_left = 2 * index + 1
            i_right = 2 * index + 2

            if i_left < heap_size and \
                    self.data_list[i_left] < self.data_list[index]:
                i_max = i_left
            if i_right < heap_size and \
                    self.data_list[i_right] < self.data_list[i_max]:
                i_max = i_right

            if i_max != index:
                self.data_list[i_max], self.data_list[index] = \
                    self.data_list[index], self.data_list[i_max]
                index = i_max
            else:
                break

    def heapify(self, is_max_heap=True):
        heap_size = len(self.data_list)
        parent = heap_size // 2

        for i in range(parent - 1, -1, -1):
            if is_max_heap:
                self.max_heapify(i, heap_size)
            else:
                self.min_heapify(i, heap_size)


if __name__ == '__main__':
    l = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    heap = Heap(l)
    h = heap.heapify()
    print(heap.data_list)
    heap.heapify(is_max_heap=False)
    print(heap.data_list)



def swap(lista, index_1, index_2):
    """The function that swap two elements in a list."""

    temp = lista[index_1]
    lista[index_1] = lista[index_2]
    lista[index_2] = temp


def sort_object(lista, object_index, end_index):
    """The function finds the sorted index of the first element in the list."""

    swap_index = object_index

    for i in range(object_index+1, end_index+1):
        if lista[i] < lista[object_index]:
            swap_index += 1
            swap(lista, swap_index, i)
    swap(lista, object_index, swap_index)
    return swap_index


def quick_sort(lista, left, right):
    """The sorting function."""

    if left < right:
        object_index = sort_object(lista, left, right)
        quick_sort(lista, left, object_index - 1)
        quick_sort(lista, object_index + 1, right)
    return lista

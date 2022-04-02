def reverse(element_list):
    start_index = 0
    end_index = len(element_list) - 1

    while start_index < end_index:
        element_list[start_index], element_list[end_index] = (
            element_list[end_index],
            element_list[start_index],
        )
        start_index += 1
        end_index -= 1
    return element_list


if __name__ == "__main__":
    element = ["a", "n", "f", "9", "t"]
    reverse(element)
    print(element)


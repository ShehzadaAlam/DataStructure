def reverse_string(data_elem):
    data = list(data_elem)
    start_index = 0
    end_index = len(data_elem) - 1
    while start_index < end_index:
        data[start_index], data[end_index] = data[end_index], data[start_index]
        start_index += 1
        end_index -= 1
    return "".join(data)


def check_palindrome(data):
    if data == reverse_string(data):
        return True
    return False


if __name__ == "__main__":
    data = "madam"
    print(check_palindrome(data))

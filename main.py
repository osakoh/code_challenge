from math import ceil


class GroupArrayElements:
    """

    """

    def __init__(self, array_elements: list, N: int) -> [list]:
        """
        :param array_elements: represents list/array which is always equal to or greater than 0
        :param N: steps to which the array should be divided(positive integer)
        """
        self.array_elements = array_elements
        self.N = N
        # final list to be returned
        self.output = []

    # @property: call function without parenthesis ()
    @property
    def array_length(self):
        """ :returns length of list/array """
        return len(self.array_elements)

    @property
    def size(self):
        """
        math.ceil: rounds a decimal number to nearest integer upwards
        this (math.ceil) was used because integer division(//) will always return 0 if the given argument is less than 1
        but math.ceil will round the decimal number to the nearest integer upwards
        :returns the number of times the array can be divided
        """
        return ceil(self.array_length / self.N)

    def add_output(self, sm_list: list):
        """ takes a list an appends to the output list """
        self.output.append(sm_list)

    @property
    def result(self):
        """
        performs the actual calculation
        :return: the output list
        """
        # loop over number of N numbers no matter the size
        for num in range(self.N):
            start = num * self.size
            stop = (num + 1) * self.size

            # print(f"start: {start} | stop: {stop}")

            # get individual list from the main list
            group = self.array_elements[start: stop]
            self.add_output(group)

        # the output list
        return self.output

# arr = [1, 2, 3, 4, 5, 6]
# n = 4
# test = GroupArrayElements(arr, n)
# print(test.result)

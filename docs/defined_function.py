def sum_up(Input, x):
    """
    Note
    ----
    This is a function to calculate the summation of two numbers.

    Parameters:

                Input: An integer as an input to perform the calculation.
                x: An integer to be used for calculation

    Returns:
                x_sum: An integer for the final result.
    """

    x_sum = Input + x
    return x_sum


def multiply(Input, y):
    """
    Parameter
    ---------
    y: An integer to be used for calculation

    Return
    ------
    y_mul: An integer for the final result.
    """
    y_mul = Input * y
    return y_mul


def stock_up(inhabitant, quantity):
    """Add more fish or shrimp to the tank.

    :param inhabitant: The type of inhabitant, either shrimp of fish
    :param quantity: The number of fish or shrimp to be added

    :raises TankIsFullError: if the tank is already full
    """

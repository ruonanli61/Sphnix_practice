class Myclass:
    """
    Perform multiple calculation for a given input.

    Parameters
    ----------

                damping: float, default=0.5
                    A factor within the range of [0.5, 1.0), which is used for the summation.
                Waving: integer, default=2
                    A factor within the range of [1, 10], wich is used for the multiplication.

    Returns
    -------
                y: A float for the final result.

    Note
    ----
    This class perform two calculations for a given input - summation and multiplication.

    Example
    -------
    >>> from Sphnix.docs.defined_class import Myclass
    >>> result = Myclass(4, 0.5, 5)
    >>> result
    22.5
    """

    def __init__(self, damping=0.5, waving=2):
        self.damping = damping
        self.waving = waving

    def summation(self, x):
        """
        Parameter
        ---------
        x: An integer to be used for calculation

        Return
        ------
        x_sum: the results for adding the input x and the damping factor
        """

        x_sum = x + self.damping
        return x_sum

    def multiplication(self, x):
        """
        Parameter
        ---------
        x: An integer to be used for calculation

        Return
        ------
        x_mul: the results for multiplying the input x and the waving factor
        """
        x_mul = x * self.waving
        return x_mul

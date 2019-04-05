import numpy as np


def allocate(district, unit):
    """ generates all possible allocations
    :param district: number of districts
    :param unit: number of units of resources
    :return 2D numpy array of all possible allocations
    """
    # one district: base case
    if district == 1:
        return np.array([[unit]])

    # allocate all units to districts 1-n
    temp = allocate(district - 1, unit)
    result = np.array([np.append(t, 0) for t in temp])

    # allocate i units to district n
    for i in range(1, unit + 1):
        temp = allocate(district - 1, unit - i)
        new_result = np.array([np.append(t, i) for t in temp])
        result = np.concatenate((new_result, result), axis = 0)

    # return
    return result


def payoff(district, unit, allocation):
    """ generates the payoff matrix
    :param district: number of districts
    :param unit: number of units of resources
    :param allocation: 2D numpy array of allocations
    :return 2D payoff matrix
    """
    vote = np.array([i for i in range(1, district + 1)])

    # size of payoff matrix
    s = allocation.shape[0]
    payoff_matrix = np.zeros((s, s))

    # fill in the payoff matrix
    for i in range(0, s):
        for j in range(i, s):

            # absolute win?
            win = sum(vote * (allocation[i] > allocation[j])) > sum(vote * (allocation[j] > allocation[i]))

            # tie?
            equal = sum(vote * (allocation[i] > allocation[j])) == sum(vote * (allocation[j] > allocation[i]))

            # if absolute win
            if win:
                payoff_matrix[i, j] = 1
                payoff_matrix[j, i] = -1

            # if lose
            elif not equal:
                payoff_matrix[i, j] = -1
                payoff_matrix[j, i] = 1
    # return
    return payoff_matrix


def analyse(payoff):
    """ return min-max and max-min of the payoff matrix
    :param payoff: the payoff matrix
    :return min-max & max-min;
            if v1 == v2, then unique optimal pure strategy exists
    """
    v1 = max(np.min(payoff, axis = 1))
    v2 = min(np.max(payoff, axis = 0))
    return v1, v2


def dominate(payoff, j, i):
    """ check if strategy j dominates i
    :param payoff: the payoff matrix
    :param j: index of strat
    :param i: index of strat
    :return boolean that represents if strat j dominates strat i
    """
    return (sum(payoff[j] >= payoff[i]) == payoff.shape[0])


def eliminate(payoff, run):
    """ calculate the indices of strategies that can be eliminated
    :param payoff: the payoff matrix
    :param run: the # of iterations you want to run
    :return a set of indices of dominated strategies
    """
    to_delete = set([])
    counter = 0
    while counter < run:
        counter += 1
        for i in range(0, payoff.shape[0]):
            for j in [t for t in range(0, payoff.shape[0]) if t != i]:
                if dominate(payoff, j, i):
                    to_delete.add(i)
                    payoff[i, :] = -1 * np.ones(payoff.shape[0])
                    payoff[:, i] = -1 * np.ones(payoff.shape[0])
    return to_delete


def keep(payoff, run):
    """ calculate the indices of strategies that might be kept
    :param payoff: the payoff matrix
    :param run: the # of iterations you want to run
    :return a set of indices of non-dominated strategies
    """
    return set(range(0, payoff.shape[0])) - eliminate(payoff, run)


if __name__ == "__main__":

    # params
    district = 10; unit = 2

    # get possible allocations
    allocation = allocate(district, unit)

    # payoff matrix
    payoff = payoff(district, unit, allocation)

    # check if there is an equilibrium
    v1, v2 = analyse(payoff)

    print('--- elimination starts here! ---')

    # keep indices
    keep = keep(payoff, 5)

    # sub payoff matrix of non-dominated strategies
    submatrix = payoff[list(keep)][:, list(keep)]

    '''
    # size of the sub payoff matrix
    s = submatrix.shape[0]

    # first (n - 1) equality 
    a_partial = submatrix

    # sum to one constraint
    sum_to_one = np.array([np.ones(s)])

    # complete (a, b)
    a = np.concatenate((a_partial, sum_to_one), axis = 0)
    b = np.append(np.zeros(s), 1.0)

    # just playing around...
    sol1 = np.linalg.solve(a_partial, np.zeros(s))

    # but linalg.solve can't solve non-square ax = b wtf?
    # sol2 = np.linalg.solve(a, b)
    '''

    print('the end!')
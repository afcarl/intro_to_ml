#A set of solvers from http://stackoverflow.com/questions/36321558/find-the-set-of-integers-for-which-two-linear-equalities-holds-true
def solve_robust(smin, smax, coef):
    """
    Return a list of lists of non-negative integers `n` that satisfy
    the inequalities,

    sum([coef[i] * n[i] for i in range(len(coef)]) > smin
    sum([(coef[i]+1) * n[i] for i in range(len(coef)]) < smax

    where coef is a list of positive integer coefficients, ordered
    from highest to lowest.
    """
    if smax <= smin:
        return []
    if smin < 0 and smax <= coef[-1]+1:
        return [[0] * len(coef)]

    c0 = coef[0]
    c1 = c0 + 1
    n_max = ((smax-1) // c1)
    solutions = []
    if len(coef) > 1:
        for n0 in range(n_max + 1):
            for solution in solve(smin - n0 * c0,
                                  smax - n0 * c1, 
                                  coef[1:]):
                solutions.append([n0] + solution)
    else:
        n_min = max(0, (smin // c0) + 1)
        for n0 in range(n_min, n_max + 1):
            solutions.append([n0])
    return solutions

def solve_intuitive(smin, smax, coef1, coef2):
    """
    Return a list of lists of non-negative integers `n` that satisfy
    the inequalities,

    sum([coef1[i] * n[i] for i in range(len(coef1)]) > smin
    sum([coef2[i] * n[i] for i in range(len(coef1)]) < smax

    where coef1 and coef2 are equal-length lists of positive integers.
    """
    if smax < 0:
        return []

    n_max = ((smax-1) // coef2[0])
    solutions = []
    if len(coef1) > 1:
        for n0 in range(n_max + 1):
            for solution in solve(smin - n0 * coef1[0],
                                  smax - n0 * coef2[0], 
                                  coef1[1:], coef2[1:]):
                solutions.append([n0] + solution)
    else:
        n_min = max(0, (smin // coef1[0]) + 1)
        for n0 in range(n_min, n_max + 1):
            if n0 * coef1[0] > smin and n0 * coef2[0] < smax:
                solutions.append([n0])
    return solutions

from scipy.optimize import minimize,root

def minimizeFunc(eqn, initial_guess, args):
    result=minimize(lambda params: eqn(params,args), initial_guess, method='BFGS')
    return result.x

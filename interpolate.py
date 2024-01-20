from scipy.interpolate import interp1d

def linear_interp(x, y):
    result_lin=interp1d(x, y, kind="linear")
    return result_lin

def cubic_interp(x, y):
    result_cub=interp1d(x, y, kind="cubic")
    return result_cub

def quadratic_interp(x, y):
    result_quad=interp1d(x, y, kind="quadratic")
    return result_quad
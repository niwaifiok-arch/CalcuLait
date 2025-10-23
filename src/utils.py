def add(*args):
    """
    Add unlimited number of parameters.
    
    Args:
        *args: Variable number of numeric arguments
        
    Returns:
        Sum of all arguments
        
    Raises:
        TypeError: If any argument is not numeric
    """
    if not args:
        return 0
    
    for arg in args:
        if not isinstance(arg, (int, float)):
            raise TypeError(f"All arguments must be numeric, got {type(arg).__name__}")
    
    return sum(args)


def subtract(*args):
    """
    Subtract unlimited number of parameters from the first.
    
    Args:
        *args: Variable number of numeric arguments
        
    Returns:
        Result of subtracting all subsequent arguments from the first
        
    Raises:
        TypeError: If any argument is not numeric
        ValueError: If no arguments provided
    """
    if not args:
        raise ValueError("At least one argument required for subtraction")
    
    for arg in args:
        if not isinstance(arg, (int, float)):
            raise TypeError(f"All arguments must be numeric, got {type(arg).__name__}")
    
    result = args[0]
    for num in args[1:]:
        result -= num
    
    return result

# CREATE A FUNCTION
def safe_divide(a: float, b: float) -> float:
    try:
        # VALIDATE ARGUMENTS
        if not isinstance(a,(int,float)): # Verify if a is a number
            raise TypeError(f"Your parameter {a} don't match with required type: {type(a).__name__}")
        if not isinstance(b,(int,float)):
            raise TypeError(f"Your parameter {b} don't match with required type: {type(b).__name__}")
        # VALIDATE ARGUMENT B
        if b == 0:
            raise ZeroDivisionError(f"b cannot be 0!")
        # PERFORMING THE OPERATION
        result: float = a / b
        # TRY-EXCEPT-ELSE-FINALLY BLOCK
    except TypeError as e:
        print(f"Type error: {e}")
    except ZeroDivisionError as e:
        print(f"Division error: {e}")
    else:
        print("Operation successful!")
        return result
    finally:
        print("Operation complete!")

safe_divide(10, 2)
safe_divide(10, 0)
safe_divide("10", 2)
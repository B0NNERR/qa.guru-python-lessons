def base_sum(a: int, b: int) -> int:
	if a is None or b is None:
		raise ValueError("Input values cannot be None")
	
	if not isinstance(a, int) or not isinstance(b, int):
		raise TypeError("Input values must be integers")
	
	return a + b

__all__ = ["base_sum"]
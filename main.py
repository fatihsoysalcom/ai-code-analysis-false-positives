def check_status(value: int) -> bool:
    """
    Checks if a value meets a certain criteria.
    This explicit if/else structure is perfectly readable and valid,
    though some linters might suggest a more concise 'return value > 0'.
    An AI might flag this as 'redundant conditional' or 'can be simplified',
    even if the developer chose it for clarity or future expansion.
    """
    if value > 0:
        return True
    else:
        return False

def process_items(items: list[int]):
    """
    Processes a list of items, demonstrating a few patterns that
    might trigger false positives in AI code analysis.
    """
    # This variable is defined for potential future use or context,
    # but in this simple example, it might be flagged as 'unused variable'
    # by an overly aggressive analyzer, leading to a false positive.
    operation_mode = "standard"

    print(f"Starting processing in {operation_mode} mode...")

    for item in items:
        # This 'if True' block is a common pattern for a placeholder
        # or a default path that might later contain complex conditions.
        # An AI might flag it as 'redundant condition' or 'unreachable code',
        # even though it's a valid design choice for extensibility.
        if True: 
            if check_status(item):
                print(f"  Item {item}: Status OK.")
            else:
                print(f"  Item {item}: Status NOT OK.")
        else:
            # This 'else' block is intentionally empty, a valid placeholder
            # for future logic. An AI might flag this as 'empty block' or 'redundant',
            # another example of a false positive on good code.
            pass 

    # A simple constant, which might be flagged as a 'magic number'
    # if it were embedded directly in a more complex calculation by some linters,
    # but here it's just a clear, self-explanatory value.
    DEFAULT_LIMIT = 10
    print(f"Processing finished. Default limit was {DEFAULT_LIMIT}.")

# --- Main execution --- 
if __name__ == "__main__":
    sample_data = [-1, 0, 5, 12, -3, 8]
    print("--- Running example with sample data ---")
    process_items(sample_data)
    print("--- Example finished ---")

    # Another function demonstrating a simple, clear pattern
    # that an AI might over-optimize or misinterpret as 'unnecessary abstraction'
    # if it's only called once, despite being good for modularity.
    def get_user_message(user_id: int) -> str:
        """
        Returns a simple message based on user ID.
        """
        if user_id > 0:
            message = f"User ID: {user_id} is active."
        else:
            message = "Invalid User ID."
        return message

    print(get_user_message(101))
    print(get_user_message(-5))

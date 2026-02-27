

def extract_action_items_llm(input_text):
    """
    Extracts all the action items from the input text and returns them as 
a string.
    
    Args:
        input_text (str): The input text that contains action items.
        
    Returns:
        str: A string containing all action items in the format "[] action 
item".
    """
    
    # Regular expression pattern to match action items
    pattern = r"-?\s*(\S+)"
    
    # Find all occurrences of action items in the input text
    matches = re.findall(pattern, input_text)
    
    # Create a string containing all action items in the format "[] action item"
    output_string = ", ".join(f"[] {match}" for match in matches)
    
    return output_string

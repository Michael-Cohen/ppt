from jinja2 import Environment, FileSystemLoader


def set_query(query_path: str, replacement: dict) -> str:
    """Dynamically creates an SQL query from a template.

    Note: Jinja2 has another feature called "template inheritance"
    for replacing whole blocks of the template. This is not used
    in this function.

    Args:
        query_path (str): Path to the SQL query template.
        replacement (dict): Dictionary {variable -> replacement value} to
            be applied.

    Returns:
        str: The query with replacements performed.
    """
    # Create a Jinja environment
    env = Environment(loader=FileSystemLoader("src/pptm"))
    # Load the template
    template = env.get_template(query_path)
    # Render the template with the dynamic content
    output = template.render(replacement)
    return output


# Example usage of set_query:
print(set_query(query_path="query.sql", replacement={"name": "last_name"}))

from jinja2 import Environment, FileSystemLoader


def set_query(query_path: str, replacement: dict) -> str:
    # Create a Jinja environment
    env = Environment(loader=FileSystemLoader("src/pptm"))
    # Load the template
    template = env.get_template(query_path)
    # Render the template with the dynamic content
    output = template.render(replacement)
    return output


# Example usage of set_query:
print(set_query(query_path="query.sql", replacement={"name": "last_name"}))

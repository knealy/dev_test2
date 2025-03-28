import requests
from bs4 import BeautifulSoup

def create_character_grid(url):
    # Fetch and parse the document
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.get_text()
    
    # Process the content character by character
    coord_dict = {}
    i = 0
    while i < len(content):
        # Look for first digit of x coordinate
        if i < len(content) and content[i].isdigit():
            x_str = content[i]
            i += 1
            # Check for possible second digit of x coordinate
            if i < len(content) and content[i].isdigit():
                x_str += content[i]
                i += 1
            
            # Next must be the special character
            if i < len(content) and not content[i].isdigit():
                char = content[i]
                i += 1
                
                # Next must be single digit y coordinate
                if i < len(content) and content[i].isdigit():
                    y = int(content[i])
                    x = int(x_str)
                    if ord(char) > 32:  # Valid unicode character
                        coord_dict[(x, y)] = char
                        # print(f"Found: x={x}, y={y}, char={char}")
                    i += 1
        else:
            i += 1
    
    # Create and print the grid
    if not coord_dict:
        print("No valid coordinates found")
        return None
        
    max_x = max(x for x, _ in coord_dict.keys())
    max_y = max(y for _, y in coord_dict.keys())
    
    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    
    for (x, y), char in coord_dict.items():
        grid[y][x] = char
    
    for row in reversed(grid):
        line = ''.join(row)
        if not all(c.isspace() for c in line):
            print(line)
            
    return grid

# Example usage
url = 'https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub'
url1 = 'https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub'
character_grid = create_character_grid(url)
character_grid1 = create_character_grid(url1)

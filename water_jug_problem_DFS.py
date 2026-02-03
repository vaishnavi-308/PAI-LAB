# Water Jug Problem using DFS (Depth First Search)

# Helper function to generate all possible next states
def get_next_states(x, y, a, b):
    states = set()

    # Fill jugs
    states.add((a, y))   # Fill Jug A
    states.add((x, b))   # Fill Jug B

    # Empty jugs
    states.add((0, y))   # Empty Jug A
    states.add((x, 0))   # Empty Jug B

    # Pour A -> B
    pour = min(x, b - y)
    states.add((x - pour, y + pour))

    # Pour B -> A
    pour = min(y, a - x)
    states.add((x + pour, y - pour))

    return states


# DFS function
def water_jug_dfs(a, b, target):
    visited = set()

    def dfs(x, y, path):
        if (x, y) in visited:
            return None

        visited.add((x, y))
        path.append((x, y))

        # Goal state
        if x == target or y == target:
            return path

        # Explore next states
        for nx, ny in get_next_states(x, y, a, b):
            result = dfs(nx, ny, path.copy())
            if result:
                return result

        return None

    return dfs(0, 0, [])


# Main program (Dynamic Input)
if __name__ == "__main__":
    a = int(input("Enter capacity of Jug A: "))
    b = int(input("Enter capacity of Jug B: "))
    target = int(input("Enter target amount: "))

    print("\n--- DFS Solution ---")
    solution = water_jug_dfs(a, b, target)

    if solution:
        for step in solution:
            print(step)
    else:
        print("No solution found")

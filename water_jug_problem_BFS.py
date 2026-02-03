from collections import deque

# MUST be defined before BFS
def get_next_states(x, y, a, b):
    states = set()

    states.add((a, y))      # Fill A
    states.add((x, b))      # Fill B
    states.add((0, y))      # Empty A
    states.add((x, 0))      # Empty B

    pour = min(x, b - y)    # Pour A -> B
    states.add((x - pour, y + pour))

    pour = min(y, a - x)    # Pour B -> A
    states.add((x + pour, y - pour))

    return states


def water_jug_bfs(a, b, target):
    visited = set()
    queue = deque([((0, 0), [])])

    while queue:
        (x, y), path = queue.popleft()

        if (x, y) in visited:
            continue

        visited.add((x, y))
        path = path + [(x, y)]

        if x == target or y == target:
            return path

        for state in get_next_states(x, y, a, b):
            if state not in visited:
                queue.append((state, path))

    return None


if __name__ == "__main__":
    a = int(input("Enter capacity of Jug A: "))
    b = int(input("Enter capacity of Jug B: "))
    target = int(input("Enter target amount: "))

    print("\n--- BFS Solution ---")
    result = water_jug_bfs(a, b, target)
    print(result if result else "No solution found")

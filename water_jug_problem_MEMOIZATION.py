def get_next_states(x, y, a, b):
    states = []

    # Fill Jug A
    if x < a:
        states.append((a, y, f"Fill Jug A ({x}->{a})"))
    # Fill Jug B
    if y < b:
        states.append((x, b, f"Fill Jug B ({y}->{b})"))
    # Empty Jug A
    if x > 0:
        states.append((0, y, f"Empty Jug A ({x}->0)"))
    # Empty Jug B
    if y > 0:
        states.append((x, 0, f"Empty Jug B ({y}->0)"))
    # Pour A -> B
    if x > 0 and y < b:
        pour = min(x, b - y)
        states.append((x - pour, y + pour, f"Pour {pour} from A -> B"))
    # Pour B -> A
    if y > 0 and x < a:
        pour = min(y, a - x)
        states.append((x + pour, y - pour, f"Pour {pour} from B -> A"))

    return states


def water_jug_memo(a, b, target):
    memo = set()

    def dfs(x, y, path, actions):
        if (x, y) in memo:
            return None, None
        memo.add((x, y))
        path = path + [(x, y)]

        if x == target or y == target:
            return path, actions

        for nx, ny, action in get_next_states(x, y, a, b):
            new_path, new_actions = dfs(nx, ny, path, actions + [action])
            if new_path:
                return new_path, new_actions

        return None, None

    return dfs(0, 0, [], [])


# Main
a = int(input("Enter capacity of Jug A: "))
b = int(input("Enter capacity of Jug B: "))
target = int(input("Enter target amount: "))

path, actions = water_jug_memo(a, b, target)

print("\n--- Memoization DFS Solution with Detailed Steps ---")
if path:
    for i, (state, action) in enumerate(zip(path[1:], actions), 1):
        print(f"Step {i}: {action} => Jug A = {state[0]}, Jug B = {state[1]}")
else:
    print("No solution found")

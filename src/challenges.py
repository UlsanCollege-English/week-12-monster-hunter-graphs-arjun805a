"""
Week 12: Monster Hunter Graphs

Complete each function using Python 3.11+.

Rules:
- Standard library only.
- Use type hints.
- Keep public function docstrings.
- Run tests with: pytest -q
"""

import heapq


def build_hunter_map(edges: list[tuple[str, str]]) -> dict[str, list[str]]:
    """Build an undirected adjacency list from route pairs.

    Each tuple represents a two-way route between two monster sighting
    locations.

    Args:
        edges: A list of route pairs, such as
            [("Old Theater", "Train Station")].

    Returns:
        A dictionary where each key is a location and each value is a list
        of neighboring locations.

    Rules:
        - Add both directions for each route.
        - Include every location that appears in the input.
        - Do not duplicate neighbors if the same route appears more than once.
    """

    graph: dict[str, list[str]] = {}

    for location_a, location_b in edges:

        if location_a not in graph:
            graph[location_a] = []

        if location_b not in graph:
            graph[location_b] = []

        if location_b not in graph[location_a]:
            graph[location_a].append(location_b)

        if location_a not in graph[location_b]:
            graph[location_b].append(location_a)

    return graph


def build_weighted_hunter_map(
    edges: list[tuple[str, str, int]]
) -> dict[str, dict[str, int]]:
    """Build an undirected weighted graph from route triples.

    Each tuple represents a two-way route with a positive danger score.

    Args:
        edges: A list of route triples, such as
            [("Old Theater", "Train Station", 4)].

    Returns:
        A nested dictionary where graph[start][end] is the danger score.

    Rules:
        - Add both directions for each route.
        - Danger scores must be positive integers.
        - If danger score is 0 or negative, raise ValueError.
        - If the same route appears more than once, keep the lowest score.
    """

    graph: dict[str, dict[str, int]] = {}

    for start, end, danger_score in edges:

        if danger_score <= 0:
            raise ValueError("Danger score must be positive.")

        if start not in graph:
            graph[start] = {}

        if end not in graph:
            graph[end] = {}

        # Keep lowest score if duplicate route appears
        if end not in graph[start]:
            graph[start][end] = danger_score
            graph[end][start] = danger_score

        else:
            lowest_score = min(graph[start][end], danger_score)
            graph[start][end] = lowest_score
            graph[end][start] = lowest_score

    return graph


def map_summary(graph: dict[str, list[str]]) -> dict[str, int]:
    """Return the number of locations and undirected routes.

    Args:
        graph: An undirected adjacency list.

    Returns:
        A dictionary with:
            - "locations": number of locations
            - "routes": number of undirected routes

    Example:
        {
            "A": ["B", "C"],
            "B": ["A"],
            "C": ["A"],
        }

        returns {"locations": 3, "routes": 2}
    """

    locations = len(graph)

    total_connections = sum(len(neighbors) for neighbors in graph.values())

    # Divide by 2 because graph is undirected
    routes = total_connections // 2

    return {
        "locations": locations,
        "routes": routes,
    }


def most_connected_location(graph: dict[str, list[str]]) -> str | None:
    """Return the location with the most neighbors.

    Args:
        graph: An undirected adjacency list.

    Returns:
        The location with the most neighbors.
        If the graph is empty, return None.
        If there is a tie, return the alphabetically first location.
    """

    if not graph:
        return None

    best_location = None
    highest_connections = -1

    for location in sorted(graph):

        connection_count = len(graph[location])

        if connection_count > highest_connections:
            highest_connections = connection_count
            best_location = location

    return best_location


def priority_hunt_order(reports: list[tuple[int, str]]) -> list[str]:
    """Return monster sighting locations from most urgent to least urgent.

    Lower priority number means more urgent.

    Args:
        reports: A list of tuples in the form (priority, location).

    Returns:
        A list of locations ordered from lowest priority number to highest.

    Requirement:
        Use heapq.
    """

    heap: list[tuple[int, str]] = []

    for priority, location in reports:
        heapq.heappush(heap, (priority, location))

    ordered_locations: list[str] = []

    while heap:

        priority, location = heapq.heappop(heap)
        ordered_locations.append(location)

    return ordered_locations


# ----------------------------
# Example Test Runs
# ----------------------------
if __name__ == "__main__":

    route_edges = [
        ("Old Theater", "Train Station"),
        ("Train Station", "City Hall"),
        ("Old Theater", "City Hall"),
        ("Old Theater", "Train Station"),  # Duplicate route
    ]

    weighted_edges = [
        ("Old Theater", "Train Station", 4),
        ("Train Station", "City Hall", 2),
        ("Old Theater", "City Hall", 7),
        ("Old Theater", "Train Station", 1),  # Lower duplicate score
    ]

    reports = [
        (3, "Old Theater"),
        (1, "City Hall"),
        (2, "Train Station"),
    ]

    hunter_map = build_hunter_map(route_edges)

    weighted_map = build_weighted_hunter_map(weighted_edges)

    print("=== Hunter Map ===")
    print(hunter_map)

    print("\n=== Weighted Hunter Map ===")
    print(weighted_map)

    print("\n=== Map Summary ===")
    print(map_summary(hunter_map))

    print("\n=== Most Connected Location ===")
    print(most_connected_location(hunter_map))

    print("\n=== Priority Hunt Order ===")
    print(priority_hunt_order(reports))
# Week 12: Monster Hunter Graphs

## Student

Name: Arjun Shahi


---

## Summary

This assignment builds both unweighted and weighted graph structures using Python dictionaries.  
The locations represent monster sighting areas, while the routes represent connections between those locations.  
The program also analyzes the graph by counting routes, finding the most connected location, and organizing monster reports using a priority queue.  
The weighted graph stores danger scores between locations.  
The hardest function was `build_weighted_hunter_map` because it needed validation and duplicate route handling with the lowest danger score.

---

## Approach

- `build_hunter_map`:
  - Created an undirected adjacency list.
  - Added routes in both directions.
  - Prevented duplicate neighbors.

- `build_weighted_hunter_map`:
  - Built a nested dictionary for weighted routes.
  - Checked that danger scores were positive.
  - Kept the smallest weight when duplicate routes appeared.

- `map_summary`:
  - Counted total locations using `len(graph)`.
  - Counted all connections and divided by 2 because the graph is undirected.

- `most_connected_location`:
  - Compared neighbor counts for every location.
  - Used alphabetical sorting to break ties.

- `priority_hunt_order`:
  - Used `heapq` as a priority queue.
  - Returned locations from lowest priority number to highest.

---

## Complexity

### `build_hunter_map`

- Time: O(E)
- Space: O(V + E)
- Why:
  - Each edge is processed once and stored in the adjacency list.

### `build_weighted_hunter_map`

- Time: O(E)
- Space: O(V + E)
- Why:
  - Each weighted edge is processed once and stored in the nested dictionary.

### `map_summary`

- Time: O(V + E)
- Space: O(1)
- Why:
  - Every neighbor list is visited once to count routes.

### `most_connected_location`

- Time: O(V log V)
- Space: O(1)
- Why:
  - Sorting the graph keys takes O(V log V).

### `priority_hunt_order`

- Time: O(N log N)
- Space: O(N)
- Why:
  - Heap insertion and removal both require logarithmic time.

---

## Edge-Case Checklist

- [x] Empty graph
- [x] One route
- [x] Duplicate routes
- [x] Disconnected locations
- [x] Tie for most connected location
- [x] Positive weighted routes
- [x] Invalid zero or negative danger score
- [x] Empty priority report list

---

## Tests

Paste the result of your test run.

```bash
pytest -q
```

Result:

```text
5 passed in 0.04s
```

---

## Assistance & Sources

AI used? Yes

If yes, what did it help with?

- Helped explain graph complexity analysis.
- Helped improve code organization and readability.
- Helped review edge cases and documentation.

Other sources used:

- Python 3.11 documentation
- heapq documentation
- Course lecture notes
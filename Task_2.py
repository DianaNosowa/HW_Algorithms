class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        num_rows, num_cols = len(grid), len(grid[0])
        visited_cells = set()
        largest_area = 0

        def calculate_area(row, col):
            """Calculates the area of an island (recursively; DFS approach)."""
            # Base case: out of bounds, water (0) or already visited cell
            if (row < 0 or row >= num_rows or
                col < 0 or col >= num_cols or
                (row, col) in visited_cells or grid[row][col] == 0):
                return 0

            visited_cells.add((row, col))
            current_area = 1

            # Traversal
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            for dr, dc in directions:
                current_area += calculate_area(row + dr, col + dc)

            return current_area

        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == 1 and (row, col) not in visited_cells:
                    island_area = calculate_area(row, col)
                    largest_area = max(largest_area, island_area)

        return largest_area

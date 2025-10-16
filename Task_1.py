class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        # If the starting pixel's color is  the target color -> no changes
        if image[sr][sc] == color:
          return image

        initial_color = image[sr][sc]
        rows, cols = len(image), len(image[0])

        def compare_color(r, c): #DFS
        # Check boundaries and color
            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                image[r][c] != initial_color
            ):
                return

            image[r][c] = color

        # Recursively visit all neighbors
            compare_color(r + 1, c)  # down
            compare_color(r - 1, c)  # up
            compare_color(r, c + 1)  # right
            compare_color(r, c - 1)  # left

        compare_color(sr, sc)

        return image

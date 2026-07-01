class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        # Count student preferences
        counts = [0, 0]
        for student in students:
            counts[student] += 1
            
        # Process sandwiches in the order they appear
        for sandwich in sandwiches:
            if counts[sandwich] > 0:
                counts[sandwich] -= 1
            else:
                # No student wants the top sandwich, process stops
                return counts[sandwich ^ 1]
                
        return 0
 
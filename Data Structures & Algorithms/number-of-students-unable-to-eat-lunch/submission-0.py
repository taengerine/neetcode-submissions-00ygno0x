class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # students -> queue, sandwiches -> stack 
        queue = deque(students)
        n = len(students)
        res = n

        for sandwich in sandwiches:
            count = 0
            while count < n and queue[0] != sandwich:
                cur = queue.popleft()
                queue.append(cur)
                count += 1

            if queue[0] == sandwich:
                queue.popleft()
                res -= 1
            else:
                break
        return res
        
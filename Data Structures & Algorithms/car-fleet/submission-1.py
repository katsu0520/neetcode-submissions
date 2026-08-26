class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position,speed))
        sorted_cars = sorted(cars, reverse=True)
        stack = []
        for pos,spd in sorted_cars:
            t = (target-pos)/spd
            if not stack or t > stack[-1]:
                stack.append(t)
        return len(stack)
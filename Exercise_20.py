"""Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given
range 0 and n.
Consider use yield"""


class DivisibleBySevenGenerator:
    def __init__(self, n):
        self.n = n

    def generate_divisible_by_seven(self):
        for i in range(1, self.n + 1):
            if i % 7 == 0:
                # print(i)
                yield i


num = int(input())
generate = DivisibleBySevenGenerator(num)
# iter=generate.generate_divisible_by_seven()
# print(next(iter))

for number in generate.generate_divisible_by_seven():
    print(number)
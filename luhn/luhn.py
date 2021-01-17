class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(' ', '')

    def valid(self):
        if not self.card_num.isdigit() or len(self.card_num) <= 1:
            return False
        else: 
            numbers = [int(number) for number in self.card_num]
            numbers.reverse()

            for index, number in enumerate(numbers):
                if index % 2 != 0:
                    numbers[index] *= 2

                if numbers[index] > 9:
                    numbers[index] -= 9

        return sum(numbers) % 10 == 0
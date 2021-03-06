#Input: A number as an integer.
#Output: The string representation of the number.


FIRST_TWENTY = ["one", "two", "three", "four", "five", "six", "seven",
                "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
                "sixteen", "seventeen", "eighteen", "nineteen"]
TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
        "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
    if number < 20:
        return FIRST_TWENTY[number - 1]
    elif number > 19  and number < 100:
        ones = number % 10
        if ones > 0:
            result = FIRST_TWENTY[ones - 1]
            number /= 10
            result = TENS[number - 2] + " " + result
            return "".join(result)
        elif ones == 0:
            number /= 10
            return TENS[number - 2]
    elif number >= 100:
        last_two_digits = number % 100
        if last_two_digits < 20 and last_two_digits > 0:
            result = FIRST_TWENTY[last_two_digits - 1]
            number /= 100
            result = FIRST_TWENTY[number - 1] + " " + HUNDRED + " " + result
            return "".join(result)
        elif last_two_digits == 0:
            number /= 100
            result = FIRST_TWENTY[number - 1] + " " + HUNDRED
            return "".join(result)
        elif last_two_digits > 20:
            ones = number % 10
            if ones > 0:
                result = FIRST_TWENTY[ones - 1]
                number /= 10
                tens = number % 10
                result = TENS[tens - 2] + " " + result
            elif ones == 0:
                number /= 10
                tens = number % 10
                result = TENS[tens - 2]
            number /= 10
            result = FIRST_TWENTY[number - 1] + " " + HUNDRED + " " + result
            return "".join(result)

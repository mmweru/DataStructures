ONES = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
TEENS = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
TENS = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
def convert_to_words(num):  
    if num == 0:  
        return "zero"  
    elif num< 0:
            return "minus " + convert_to_words(abs(num))
    elif num< 10:
            return ONES[num]
    elif num< 20:
            return TEENS[num - 10]
    elif num< 100:
            return TENS[num // 10] + (" " + convert_to_words(num % 10) if num % 10 != 0 else "")
    elif num< 1000:
            return ONES[num // 100] + " hundred" + (" and " + convert_to_words(num % 100) if num % 100 != 0 else "")
    elif num< 1000000:
            return convert_to_words(num // 1000) + " thousand" + (" " + convert_to_words(num % 1000) if num % 1000 != 0 else "")
    elif num< 1000000000:
            return convert_to_words(num // 1000000) + " million" + (" " + convert_to_words(num % 1000000) if num % 1000000 != 0 else "")

num = int(input("Enter a number: "))
words = convert_to_words(num)  
print(words)  
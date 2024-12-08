import re

with open("input.txt", "r") as file:
    input = file.read()


def mul_sum(s):
    ans = 0
    for m in re.findall(r"mul\(\d+,\d+\)", s):
        x, y = [int(n) for n in m[4:-1].split(",")]
        ans += x * y
    return ans


print(mul_sum(input))

# RE to match substrings where do() is active. Need DOTALL so the .* matches \n's
# Without it, a do() that spans multiple lines wouldn't be matched.
do = r"(?:^|do\(\)).*?(?:don't\(\)|$)"
print(sum(mul_sum(s) for s in re.findall(do, input, flags=re.DOTALL)))

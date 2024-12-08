reports = []
with open("input.txt", "r") as file:
    for line in file:
        reports.append([int(level) for level in line.split()])


def is_safe(l):
    return all(1 <= l[i] - l[i - 1] <= 3 for i in range(1, len(l))) or all(
        1 <= l[i - 1] - l[i] <= 3 for i in range(1, len(l))
    )


def is_mostly_safe(report):
    return is_safe(report) or any(
        is_safe(report[:i] + report[i + 1 :]) for i in range(len(report))
    )


print(sum(map(is_safe, reports)))
print(sum(map(is_mostly_safe, reports)))
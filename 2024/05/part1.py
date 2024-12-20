rules = {}
total = 0
with open("input.txt", "r") as file:
    print("Reading rules")
    for line in file:
        line = line.strip()
        if line == "":
            break
        before, after = map(int, line.split("|"))
        if before not in rules:
            rules[before] = set()
        rules[before].add(after)

    print(f"rules: {rules}")
    print("Reading pages")
    for line in file:
        pages = list(map(int, line.strip().split(",")))
        isGood = True
        for i, page in enumerate(pages):
            if page not in rules:
                continue
            rule = rules[page]
            followingPages = pages[i + 1:]
            for followingPage in followingPages:
                if followingPage not in rule:
                    isGood = False
                    break
            if isGood == False:
                break
        if isGood:
            middlePage = pages[len(pages) // 2]
            total += middlePage
            print(f"{','.join(map(str, pages))} (good, {middlePage})")
print(total)

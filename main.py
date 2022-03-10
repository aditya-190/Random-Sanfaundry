import json
import random
import re
import sys
import webbrowser


# 1. DSA
# 2. Python
# 3. Java
# 4. C++
# 5. C
# 6. OOPS
# 7. LINUX
# 8. MONGODB
# 9. MYSQL
# 10 .COMPUTER FUNDAMENTAL\n11. OS
# 12. COMPUTER NETWORK
# 13. DBMS
# 14. RDBMS
# 15. HTML
# 16. CSS
# 17. JAVASCRIPT"

def escape_special_characters(inputString):
    return inputString.translate(str.maketrans(
        {"+": r"\+", "-": r"\-", "]": r"\]", "\\": r"\\", "^": r"\^", "$": r"\$", "*": r"\*", ".": r"\."}))


def select_random_url():
    section = sys.argv[1].strip()
    topic = sys.argv[2].strip()

    section = escape_special_characters(section)
    topic = escape_special_characters(topic)

    data = json.load(open('list.json'))
    temporary = data

    if section:
        print("Inside Section")
        temporary = list(filter(lambda datum: re.search(section, datum["Section"], re.IGNORECASE), temporary))

    if topic:
        print("Inside Topic")
        temporary = list(filter(lambda datum: re.search(topic, datum["Topic"][0], re.IGNORECASE), temporary))

    if temporary:
        print("Inside Temp")
        return random.choice(temporary)["URL"][0]

    else:
        print("Inside Else")
        return random.choice(data)["URL"][0]


webbrowser.open(url=select_random_url())

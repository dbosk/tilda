from queue import Queue

def make_children(queue):
    number, string = queue.get()

    if number == 100:
       return True, string

    queue.put((number+7, f"({string})+7"))
    queue.put((number-7, f"({string})-7"))
    queue.put((number*7, f"({string})*7"))
    if number%7 == 0:
        queue.put((number/7, f"({string})/7"))

    return False, None

def main():
    queue = Queue()
    queue.put((0, "0"))

    found = False
    while queue and not found:
        found, solution = make_children(queue)

    print(f"{solution} = 100")

if __name__ == "__main__":
    main()

from queue import Queue

def make_children(number, string):
    if number == 100:
       return True, string

    q.put(tuple(tal+7, f"{string}+7"))
    q.put(tuple(tal-7, f"{string}-7"))
    q.put(tuple(tal*7, f"{string}*7"))
    if tal%7 == 0:
        q.put(tuple(tal/7, f"{string}/7"))

    return False, None

def main():
    queue = Queue()
    queue.put(0)

    found = False
    while queue and not found:
        found, solution = make_children(queue)

    print(f"{solution} = 100")

if __name__ == "__main__":
    main()

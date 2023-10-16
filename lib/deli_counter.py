def line(katz_deli):
    if not katz_deli:
        print("The line is currently empty.")
        return

    line_message = "The line is currently:"
    for index, customer in enumerate(katz_deli, start=1):
        line_message += f" {index}. {customer}"
    print(line_message)

def take_a_number(katz_deli, name):
    katz_deli.append(name)
    position = len(katz_deli)
    print(f"Welcome, {name}. You are number {position} in line.")

def now_serving(katz_deli):
    if not katz_deli:
        print("There is nobody waiting to be served!")
    else:
        serving_customer = katz_deli.pop(0)
        print(f"Currently serving {serving_customer}.")

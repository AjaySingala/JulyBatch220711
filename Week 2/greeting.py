def greet(first_name, last_name=None):
    if last_name is not None:
        return f"Hello, {first_name} {last_name}"
    else:
        return f"Please pass fname and lname"

#if __name__ == "__main__":
#    print(greet("ajay", "singala"))

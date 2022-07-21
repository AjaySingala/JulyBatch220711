# # variable scoping.
# x = 'global'

# def foo():
#     x = "Enclosing"
#     def bar():
#         x = "local"
#         print(x)
#         print(y)

#     bar()


# foo()


# # Modifying variables out of scope.
# x = 20
# y = 60
# def foo():
#     print("Executing foo()...")
#     global x, y
#     x = 40
#     print("Inside", x)

# print("Before", x)
# foo()
# print("After", x)


# nonlocal.
y = 100
def foo():
    x = 20
    global y

    def bar():
        nonlocal x
        x = 40

    bar()
    print(x)

foo()

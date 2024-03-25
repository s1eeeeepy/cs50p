def main():
    while True:
        frac = input("Fraction: ").strip()
        if gauge(convert(frac)):
            print(gauge(convert(frac)))
            break
        else:
            continue


def convert(frac):
    try:
        spl = frac.split("/")
        if int(spl[0]) <= int(spl[-1]):
            return int(spl[0]) / int(spl[-1]) * 100
    except (NameError, ValueError, ZeroDivisionError):
        return False


def gauge(percentage):
    try:
        if percentage <= 1:
            return "E"
        if percentage >= 99:
            return "F"
        else:
            return f"{round(percentage)}%"
    except TypeError:
        return False


if __name__ == "__main__":
    main()


# def main():
#     while True:
#         frac = input("Fraction: ").strip()
#         try:
#             spl = frac.split("/")
#             if spl[0].isdigit() and spl[-1].isdigit() and int(spl[0]) <= int(spl[-1]):
#                 return gauge(convert(frac))
#         except (NameError, ValueError, ZeroDivisionError):
#             continue


# def convert(frac):
#     return eval(frac) * 100


# def gauge(percentage):
#     if percentage <= 1:
#         return "E"
#     if percentage >= 99:
#         return "F"
#     else:
#         return f"{round(percentage)}%"


# if __name__ == "__main__":
#     print(main())

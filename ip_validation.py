def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    validation = 0
    try:
        nums = ip.strip().split(".")
        if len(nums) != 4:
            return False
        for n in nums:
            if int(n) in range(0, 256):
                validation += 1
        if validation == 4:
            return True
        else:
            return False
    except ValueError:
        return False


if __name__ == "__main__":
    main()

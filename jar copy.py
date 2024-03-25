class Jar:
    def __init__(self, capacity=12):
        if capacity < 1:
            raise ValueError("Capacity can't be less than 1")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Amount to deposit must be non-negative")
        if self._size + amount > self._capacity:
            raise ValueError("The jar is full")
        self._size += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Amount to withdraw must be non-negative")
        if self._size - amount < 0:
            raise ValueError("Not enough cookies in the jar")
        self._size -= amount

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size


jar = Jar()


print(jar.capacity)
print(jar.size)

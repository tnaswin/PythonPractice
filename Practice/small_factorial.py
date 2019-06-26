
class Factorial:

    def get_input(self):
        t, n = 0, 0
        number = []
        while not int(t) in range(1, 101):
            t = int(input("Enter no.of test cases required (1 - 100): "))
        print("Enter %d test cases : " %t)
        for x in range(0, t):
            while not int(n) in range(1, 101):
                n = int(input())
                number.append(n)
            n = 0
        for f in number:
            factorial(f)

    def factorial(self, f):
        fact = 1
        for i in range(1, f+1):
            fact = fact * i
        print("Factorial of ", f, "is", fact)


if __name__=="__main__":
    f = Factorial()
    f.get_input()

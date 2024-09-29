
#Write lambdas and laske here

summation = (lambda x, y: x + y)
multiplication = (lambda x, y: x * y)

def compute(f, numbers):
    
    #Your code here
    result = 0
    if len(numbers) == 0:
        return 0
    elif len(numbers) == 1:
        return numbers[0]
    else:
        result = f(numbers[0], numbers[1])
        for i in range(2, len(numbers)):
            result = f(result, numbers[i])
    return result


#Don't touche lines below
if __name__ == "__main__":
    numbers = [1,5,8,11,3]
    print(compute(multiplication, numbers))
    print(compute(summation, numbers))

    numbers = [4]
    print(compute(multiplication, numbers))
    print(compute(summation, numbers))

    numbers = []
    print(compute(multiplication, numbers))
    print(compute(summation, numbers))

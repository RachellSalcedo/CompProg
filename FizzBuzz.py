for each in range(1, 100):
    if each % 3 == 0 and each % 5 == 0:
        print('FizzBuzz')
    elif each % 5 == 0:
        print('Buzz')    
    elif each % 3 == 0:
        print('Fizz')

    else: 
        print(each)
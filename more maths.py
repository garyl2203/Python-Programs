import random


  
print("The answer is", 2*2)

print("There are <", 2**32, "> possibilities!", sep=" ")

'''x = int(input("Please enter an integer: "))

if x < 0:
     x = 0
     print('Negative changed to zero')
elif x == 0:
     print('Zero')
elif x > 1 and x < 10:
     print('Single')
else:
     print('More')
'''

# measure some strings

words = ['cat','window', 'defense' ]

for w in words:
    print(w, len(w))
    
range(5, 10)



# prints out primes and composites

for n in range(2, 10):
    for x in range(2,n):
        if n % x == 0:
            print(n, 'equals', x, '*' , n//x)
            break
    else:
        #loop fell through without finding a factor
        print(n, 'is a prime number')

# simple for loop

languages = ["C", "C++", "Perl", "Python"]

for x in languages:
    print(x)



#range

range(10)

print(list(range(10)))
print(list(range(4,50,5)))


#adding up a sum of numbers up to 100

n = 100
sum = 0
for counter in range(1,n+1):
    sum = sum + counter

print("Sum of 1 until %d: %d" % (n,sum))


#another way of adding up to 100
print('another way of adding up to 100')

n = 100
s = 0

counter = 1
while counter <= n:
    s = s + counter
    counter += 1

print("Sum of 1 until %d: %d" % (n,s))


#adding odd numbers
print('adding all odd nbrs from 1 to 10')
n=10
s=0

counter = 1
while counter <= n:
    s = s + counter
    counter = counter + 2
    
print("Sum of odd numbers from 1 until %d: %d" % (n,s))




#scans a list, adds an extra item on list


colours = ["red"]
for i in colours[:]:
    if i == "red":
        colours += ["black"]
    if i == "black":
        colours += ["white"]
print(colours)


# whats your name?
'''
while True:
     name = input("What's your name?\n")
     print("Ok, so your name is" , name ,"?")

     
     pos_term = ["yes", "here", "yeah", "yeh", "hi", "hello"]  #term we want to search for
     neg_term = ["no" , "what", "huh" , "nah", "not" , "telling"]
     raw_input = input()
     words = raw_input.lower().split()
     print(raw_input)

     if any(x in words for x in pos_term):
       print("Ok", name, "let's start our Pokemon adventure!")
       break
      
     elif any(x in words for x in neg_term):
       print("Ok then, can you tell me who you are?")
       

     else: #if the player types in other stuff
       print("That's not the answer I was expecting.")
'''


'''

#guessing a random number game

n = 50
to_be_guessed = int(n * random.random()) + 1
guess = 0


print(random.random())

print("Let's guess a number between 1 and %d!" % (n) )
while guess != to_be_guessed:
    guess = int(input("New number: "))
    if guess > 0:
        if guess > to_be_guessed:
            print("Number too large")
        elif guess < to_be_guessed:
            print("Number too small")
    else:
        print("Sorry that you're giving up!")
        break
else:
    print("Congratulation. You made it!")
    quit()


'''

l =[1,2,3,4,5]

sum=0

for element in l:
    sum+=element
    
print (sum)



def foo(first, second, third, *therest):
    print("First: %s" %(first))
    print("Second: %s" %(second))
    print("Third: %s" %(third))
    print("And all the rest... %s" %(list(therest)))

foo(1,2,3,4,5,6,7,88)



foo(1,2,3)




'''class Sigmoid(Layer):
    def __init__(self, layer):
        Layer.__init__(self, [layer])

    def _sigmoid(self, x):
        """
        This method is separate from `forward` because it
        will be used with `backward` as well.

        `x`: A numpy array-like object.
        """
        return 1. / (1. + np.exp(-x)) # the `.` ensures that `1` is a float

    def forward(self):
        input_value = self.inbound_layers[0].value
        self.value = self._sigmoid(input_value)'''
      

'''
class MSE(Layer):
    def __init__(self, y, a):
        """
        The mean squared error cost function.
        Should be used as the last layer for a network.
        """
        # Call the base class' constructor.
        Layer.__init__(self, [y, a])

    def forward(self):
        """
        Calculates the mean squared error.
        """
        # NOTE: We reshape these to avoid possible matrix/vector broadcast
        # errors.
        #
        # For example, if we subtract an array of shape (3,) from an array of shape
        # (3,1) we get an array of shape(3,3) as the result when we want
        # an array of shape (3,1) instead.
        #
        # Making both arrays (3,1) insures the result is (3,1) and does
        # an elementwise subtraction as expected.
        y = self.inbound_layers[0].value.reshape(-1, 1)
        a = self.inbound_layers[1].value.reshape(-1, 1)
        m = self.inbound_layers[0].value.shape[0]

        diff = y - a
        self.value = np.mean(diff**2)
'''
'''
    def forward(self):
        """
        Perform the sigmoid function and set the value.
        """
        input_value = self.inbound_layers[0].value
        self.value = self._sigmoid(input_value)

    def backward(self):
        """
        Calculates the gradient using the derivative of
        the sigmoid function.
        """
        # Initialize the gradients to 0.
        self.gradients = {n: np.zeros_like(n.value) for n in self.inbound_layers}
        # Sum the derivative with respect to the input over all the outputs.
        for n in self.outbound_layers:
            grad_cost = n.gradients[self]
            sigmoid = self.value
            self.gradients[self.inbound_layers[0]] += sigmoid * (1 - sigmoid) * grad_cost


for t in trainables:
        # Change the trainable's value by subtracting the learning rate
        # multiplied by the partial of the cost with respect to this
        # trainable.
        partial = t.gradients[t]
        t.value -= learning_rate * partial
'''


#help('modules')




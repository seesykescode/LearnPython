# x is equal to the string "there are %d typs of people." where %d = the number 10
x = "There are %d types of people." % 10

# binary's value is equal to the string "binary"
binary = "binary"

# the variable do_not is equal to the string "don't"
do_not = "don't"

# variable y is equal to the string literal "those who know %s and those who %s". the first %s is equal to the value of binary and the second is equal to the value of do_not
y = "Those who know %s and those who %s." % (binary, do_not)

#prints the contents of variable x above
print x
#prints the contents of variable y above
print y

#prints the string "I said: %r." where %r equals variable x above
print "I said: %r." % x
#prints the string "I said: %s." where %s equals variable y above
print "I also said: '%s'." % y

# the variable hilarious equals False
hilarious = False
# joke_evaluation is equal to the string "Isn't that joke so funny ?! %r" %r is a return string
joke_evaluation = "Isn't that joke so funny?! %r"

#prints the string from the joke_evaluation variable and makes %r equal to False (the value of the hilarious variable)
print joke_evaluation % hilarious

# w is equal to the string "This is the left side of..."
w = "This is the left side of..."
# e is equal to the string "a string with a right side."
e = "a string with a right side."

# prints both the variable w and e together
print w + e

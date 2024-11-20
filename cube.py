
 #Function to return the cube of a number
def cb(num):
  return num * num * num

      # Loop through numbers from 0 to 19
for i in range(20):
  # Check if the number is odd
  if i % 2 != 0:
    # Print the cube of the number using the cb() function
    print(cb(i))
  else:
    # Print the number itself if it is
    # even
    print(i)

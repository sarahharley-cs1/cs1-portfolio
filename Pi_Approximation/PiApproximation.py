#PiApproximation


"""This program approximates pi using the infinite sum when the user gives
an error tolerance."""




print("We are finding the minimum number of terms needed to get an approximation of pi accurate within our error tolerance.")
print("")

error = float(input("Enter error tolerance: "))

pi = 3.14159265358979

print("")
print("Number \t Pi Approximation")


piApprox = 0
counter = 1



while error <= abs(piApprox - pi):
    piApprox = piApprox + (4 * ((-1)**(counter + 1))) / (2*counter - 1)
    print(f"{counter} \t\t {piApprox: .6f}")
    counter = counter + 1
    
    




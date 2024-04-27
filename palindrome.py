class A:
    def reverse(self,n):
        s=str(n)
        return int( s[::-1])
class B(A):
    def palindrome(self,n):
        if self.reverse(n)==n:
            print("palindrome")
        else:print("not palindrome")
B().palindrome(123)


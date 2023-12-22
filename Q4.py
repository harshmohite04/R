class Upper:

    def get_string(self):
        a = input("Enter the text")
        upperdone = a.upper()
        return upperdone

    def print_string(self,upperdone):
        print(f"String is {upperdone}")




uppercase = Upper()

a = uppercase.get_string()
uppercase.print_string(a)



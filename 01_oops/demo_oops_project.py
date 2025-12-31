class Chat:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()
        
    def menu(self):
        user_input = input('''\n Welcome user! 
                           1. press 1 to signin 
                           2. press 2 to signup 
                           3. press 3 to write a post 
                           4. press 4 to message a friend 
                           5. press an other key to exit''')
        
        if user_input == '1':
            self.signin()
        elif user_input == '2':
            self.signup()
        elif user_input == '3':
            self.write_post()
        elif user_input == '4':
            self.frined_msg()
        else:
            exit()
            
    def signup(self):
        self.username = input("Enter your username: ")
        self.password = input("Enter your password: ")
        print("You are now signed up!!")
        self.menu()
            
    def signin(self):
        if self.username == '' and self.password == '':
            print("Please signup first by pressing 2 in menu!!!")
            
        else:
            uname = input("Enter your username: ")
            pswd = input("Enter your password: ")
            
            if self.username == uname and self.password == pswd:
                print("you are sucessfully logined!!")
                self.loggedin = True
            else:
                print("Enter your correct password/username or signup again!!")
                
        self.menu()
    
    def write_post(self):
        if self.loggedin == True:
            post = input("Enter your post content: ")
            print(f"You have successfully posted this {post}")
        else:
            print("Your are not logged in. please sign in first")
            
        self.menu()
        
    def frined_msg(self):
        if self.loggedin == True:
            post = input("Enter your msg you want to send: ")
            frnd = input("whom do you want to send the msg: ")
            print(f"You have successfully send this {post} to {frnd}")
        
        else:
            print("Your are not logged in. please sign in first")
            
        self.menu()   
        
if __name__ == "__main__":
    # print(__name__)
    obj = Chat()
    
# print(__name__)
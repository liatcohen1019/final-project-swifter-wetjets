import pygame
#import your controller

def main():
    pygame.init()
my_list=[]
for i in range (10):
  my_list.append(int(input()))
print(my_list)

    #Create an instance on your controller object
    #Call your mainloop
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()

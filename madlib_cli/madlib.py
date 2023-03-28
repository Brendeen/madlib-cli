from template import read_template, parse_template, merge


def main():
    name = input("Welcome to Madlib-cli! Please input your name... ")
    print(f"""
    Hello {name}, I want to play a game...
    
    Enter a corresponding descriptive word
    to fill in the blanks...or DIE!!!
               
                           
                           
                           
                           - not really...
""")


read_template("../assets/dark_and_stormy_night_template.txt")
parse_template()
merge()

if __name__ == "__main__":
    main()

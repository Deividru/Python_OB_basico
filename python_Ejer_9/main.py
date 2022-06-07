# how ridiculous is it?
class Shark:
    def __init__(self, *args):
        self.name = args[0]
        self.age = args[1]


def main():
    user = Shark('jack', 'young')
    print(user.name, user.age, sep=' || ')
    user.__init__('conor', user.age)
    print(user.name, user.age, sep=' | ')
    user.age = "old"
    user.name = "pipo"
    print(user.name, user.age, sep=' | ')


if __name__ == "__main__":
    main()




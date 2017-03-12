class Noun:
    def __init__(self, name, image):
        self.name = name
        self.image = image

    def print_name(self):
        print("Noun name: " + self.name)

    def get_name(self):
        return self.name

    def get_image(self):
        return self.image

    def define_actions(self, actions):
        self.actions = actions

    def get_actions(self):
        return self.actions;

    def __getitem__(self):
        return self.name

if __name__ == "__main__":
    print("Class Object")

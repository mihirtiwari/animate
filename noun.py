class Object:
    def __init__(self, name, image):
        if not isinstance(name, basestring):
            raise TypeError("'name' must be of type 'str'")
        self.name = name
        self.image = image

    def print_name(self):
        print("Noun name: " + self.name)

    def get_name(self):
        return self.name

    def get_image(self):
        return self.image

    def define_actions(self, actions):
        if not isinstance(actions, dict):
            raise TypeError("'actions' must be of type 'dict'")
        else:
            self.actions = actions

    def get_actions(self):
        return self.actions;

if __name__ == "__main__":
    print("Class Object")

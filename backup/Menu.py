from client import client


class Menu():
    """Handle menu generation"""
    def generate_menu(self, prompts: list):
        """Generate a list of options for the user to choose from"""
        menu_array = []
        for item in prompts:
            menu_array.append(f"{item}")
        return menu_array

    def list_directory(self, directory, type):
        """List a given directory"""
        list = client.lsinfo(directory)
        list_array = []

        for item in list:
            list_array.append(item[type])
        return list_array

    def return_query_results(self, type, query):
        """Return results of a query"""
        return_type = ["artist", "album", "title"]
        if type == return_type[0]:
            result = client.find(return_type[0], query)
        elif type == return_type[1]:
            result = client.find(return_type[1], query)
        elif type == return_type[2]:
            result = client.find(return_type[2], query)
        else:
            pass
        return result
from django import forms


# region Real World Example
class PersonForm(forms.Form):
    name = forms.CharField(max_length=100)  # Charfield support the creation, max_length -> customized
    birth_day = forms.DateField(required=False)  # DateField support the creation, required-> customized


# endregion

# region Use Cases
class A:
    pass


if __name__ == '__main__':
    a = A()
    b = A()
    print(id(a) == id(b))
    print(a, b)

    # endregion
    # region
    import json
    import xml.etree.ElementTree as etree


    class JsonDataExtractor:
        def __init__(self, filepath):
            self.data = dict()
            with open(filepath, mode='r', encoding='utf-8') as f:
                self.data = json.load(f)

            @property
            def parsed_data():
                return self.data


    class XmlDataExtractor:
        def __init__(self, filepath):
            self.tree = etree.parse(filepath)

            @property
            def parsed_data():
                return self.tree


    def dataextraction_factory(filepath):
        """
        A factory method.
        :return an instance of JsonDataExtractor of XmlDataExtractor, depending on the extension of the input file path
        """
        if filepath.endwith('json'):
            extractor = JsonDataExtractor
        elif filepath.endwith('xml'):
            extractor = XmlDataExtractor
        else:
            raise ValueError(f'Cannot extract data from {filepath}')
        return extractor(filepath)


    def extract_data_from(filepath):
        """
        a wrapper of dataextraction_factory
        add exception handling
        """
        factory_obj = None
        try:
            factory_obj = dataextraction_factory(filepath)
        except ValueError as e:
            print(e)
        return factory_obj

    def main():
        """
        demonstrates how the factory design pattern can be used.
        The first part makes sure that exception handling  is effective
        The next part shows how to work with the Json files using factory method.
        The final part shows how to work with the XML files using factory method.

        """
        wrong_file_path = \
            r'A:\New folder\design_pattern\Masterin_Python_Design_Patternm\Chapter_1_Factory_Pattern\person.sq3'
        xml_file_path = \
            r'A:\New folder\design_pattern\Masterin_Python_Design_Patternm\Chapter_1_Factory_Pattern\person.sxml'
        json_file_path =\
            r'A:\New folder\design_pattern\Masterin_Python_Design_Patternm\Chapter_1_Factory_Pattern\movies.json'
        sqlite_factory = extract_data_from(wrong_file_path)
        print()
        json_factory = extract_data_from(json_file_path)
        json_data = json_factory.parsed_data
        print(f'Found {len(json_data)} movies')
        # json part
        for movie in json_data:
            print(f"Title: {movie['title']}")
            year = movie['year']
            if year:
                print(f'Year: {year}')
                director = movie['director']
                if director:
                    print(f'Director: {director}')
                    genre = movie['genre']
                    if genre:
                        print(f"Genre: {genre}")
                        print()
        # XML part
        xml_factory = extract_data_from(xml_file_path)
        xml_data = xml_factory.parsed_data
        liars = xml_data.findall(f".//person[lastName='Liar']")
        print(f'found: {len(liars)} persons')
        for liar in liars:
            firstname = liar.find('firstName').text
            print(f'first name: {firstname}')
            lastname = liar.find('lastName').text
            print(f'last name: {lastname}')
            [print(f"phone number ({p.attrib['type']}):", p.text)
             for p in liar.find('phoneNumbers')]
            print()
    # endregion

import re

class Tag(object):
    """
    Objects of this class define an XML tag
    Properties:
    _element - the actual XML tag. _element holds element;s name (string)
    -type - type of the tag: opening, closing, one-liner (enum)
    """

    def __init__(self, element, type):
        self._element = element
        self._type = type

    @property
    def element(self):
        return self._element

    @element.setter
    def element(self, element):
        if element is not None:
            self._element = element

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self,type):
        if type is not None:
            self._type = type


# End of Tag class definition

class TagsDictionary(object):
    """
    Object of this class holds Tag class objects as keys and the number of such Tag as value in one XML file
    The methods of this class decide if the XML file has a correct number of opening and closing tags
    """
    def __init__(self):
        self._dictionary = {}

#    def to_string(self):

    def add(self, obj):
        if obj is not None:
            if obj in self._dictionary:
                self._dictionary[obj] += 1
            else:
                self._dictionary[obj] = 1



#TODO: Add logic

# End of TagsDictionary class

class TagFinder(object):
    """
    This class is used as a function to find XML tags in a given string
    Its properties are RegExes for opening and closing tags.
    Te find_tags() method receives a line as an argument and returns Tag class object if tag was found
    or empty Tag object
    Usage: my_tag_obj = my_tagfinder_obj.find_tag("A line that is supposed to contain XML tag")
    
    """

    def __init__(self):
        self._open_tag_regex = re.compile("<(\w+/?)[>\s]")
        self._close_tag_regex = re.compile(".*?(</(\w+)>)")
        #TODO: Add one_liner tag regex

    def find_tag(self, line):
        if self._open_tag_regex.search(line):
            res = self._open_tag_regex.search(line) # Do we call for this function twice???
            type = "Opening"
        elif self._close_tag_regex.search(line):
            res = self._open_tag_regex.search(line) # Do we call for this function twice???
            type = "Closing"
        else:
            res = None
            type = None
        if res is not None:
            print res.group(1)
        new_tag = Tag(res.group(1), type)
        new_tag.type = type
        return new_tag
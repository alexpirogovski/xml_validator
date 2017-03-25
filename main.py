from xml_validator_classes import *

if __name__ == "__main__":
    xml = [
                "<xml>",
                "<name gender=\"men\">Ashot</name>",
                "<user>tosha</user>",
                "<another_tag>tosha</user>",
                "<tag>tosha</teg>",
                "<last_tag/>",
                "</xml>"
            ]

    my_table = TagsDictionary( )
    my_finder = TagFinder( )
    my_dict = {}

    my_finder = TagFinder()
    for line in xml:
        new_tag = my_finder.find_tag(line)
        if new_tag in my_dict:
            my_dict[new_tag] += 1
        else:
            my_dict[new_tag] = 1

    print my_dict.__len__()






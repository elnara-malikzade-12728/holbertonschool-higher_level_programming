import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a dictionary into an XML file."""
    # 1. Create the root tag <data>
    root = ET.Element('data')

    # 2. Add each key-value pair as a child tag
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)  # XML only stores strings

    # 3. Wrap the root in a tree and write to file
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """Deserialize an XML file into a dictionary."""
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        # Reconstruct the dictionary by looping through child tags
        dictionary = {}
        for child in root:
            dictionary[child.tag] = child.text

        return dictionary
    except FileNotFoundError:
        return None
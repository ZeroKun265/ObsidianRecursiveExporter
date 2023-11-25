import argparse
import logging
import hashlib
import re
def generate_unique_id(s):
   return hashlib.sha256(s.encode()).hexdigest()

def init():
    # Create the parser
    parser = argparse.ArgumentParser(description='A way to export all notes linked to one main note in an obsidian vault inspired by klalle/ObsidianToHtmlConverter')

    # Add the arguments
    parser.add_argument('mainFile', type=str, help='Path to the main file')
    parser.add_argument('--exportToHTML', action='store_true', help='Export to HTML')
    parser.add_argument('--downloadImages', action='store_true', help='Download images')
    parser.add_argument('--logLevel', type=str, choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'], default='INFO', help='Set the logging level')


    # Parse the arguments
    args = parser.parse_args()

    # Create a logger
    logger = logging.getLogger(__name__)

    # Set the level of logging. DEBUG is the lowest level, so it will capture all logs.
    logger.setLevel(10 if args.logLevel == 'DEBUG' else 20 if args.logLevel == 'INFO' else 30 if args.logLevel == 'WARNING' else 40 if args.logLevel == 'ERROR' else 50 if args.logLevel == 'CRITICAL' else 20)

    # Create a console handler
    handler = logging.StreamHandler()

    # Create a formatter and add it to the handler
    formatter = logging.Formatter('[%(asctime)s - %(levelname)s]: %(message)s')
    handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(handler)
    return logger, args

class Link():
   def __init__(self, file: str, header: str, rename: str, visual: bool) -> None:
       self.file = file.strip(" ")
       self.header = header.strip(" ")
       self.rename = rename.strip(" ")
       self.visual = visual
       self.id = generate_unique_id(f"{self.file}{self.header}{self.rename}{'y' if self.visual else 'n'}")

   def __str__(self):
       return f"Link(\n    file='{self.file}'\n    header='{self.header}'\n    rename='{self.rename}'\n    visual={self.visual}\n    id='{self.id}'\n)"


def find_links_in_line(line):
    pattern = r'\!\[\[([^\]]*)\]\]|\[\[([^\]]*)\]\]'
    for (link) in re.findall(pattern, line):
        # We create a Link object from the data we have
        # Link structure: <OptionalEsclamationMarkForVisual>[[<Filename>#<OptionalHeader>|<OptionalRename>]]
        print(link)
        # Attachments will have this format (<content>, "") while 
        # Files will have this format ("", <content>)
        lVisual = True if link[0] else False 
        content = link[0] if link[0] else link[1]
        # Now we find all the details of the content
        lRename = ""
        if "|" in content:
            lRename = content.split("|")[1]
            file_and_header = content.split("|")[0]
        else:
            lRename = ""
            file_and_header = content

        lFile = file_and_header.split("#")[0] 
        lHeader = file_and_header.split("#")[1] if len(file_and_header.split("#")) == 2 else ""
        newLink = Link(lFile, lHeader, lRename, lVisual) 
        print(newLink)

        

def main():
    logger, args = init()
    logger.info(f"""Selected mode: Export {args.mainFile} {'to HTML' if args.exportToHTML else 'to Markdown'} {'while downloading images from the web' if args.downloadImages else 'without downloading images from the web'} """)
    logger.info(f"Opening main file {args.mainFile}")
    data = []
    with open(args.mainFile,"r",encoding='utf-8') as readfile:
        data = readfile.readlines()

    for line in data:
        find_links_in_line(line)

if __name__ == "__main__":
    main()
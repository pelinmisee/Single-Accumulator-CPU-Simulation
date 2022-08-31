class Text:
    def __init__(self,text_file):
        self.text_file=text_file

    def read_text(self):
        with open(self.text_file) as file:
            content=file.read()
            return content
    def total_of_row(self):
        count=0
        with open(self.text_file) as file:
            for line in file:
                count+=1
            return count
    def getting_line(self,which_line):
        with open(self.text_file) as file:
            count=0
            for line in file:
                count+=1
                if count==which_line:
                    return (line)




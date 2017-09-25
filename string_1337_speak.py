#1337Speak
replacements = ('A', '4'), ('E', '3'), ('G', '6'), ('I', '1'), ('O', '0'), ('S', '5'), ('T', '7')
my_paragraph = "\nGiven a paragraph of text as a string, print the paragraph in leetspeak. To translate a string to leetspeak, you need to replace make thefollowing character replacements (treat all input characters as uppercase)".upper()

new_paragraph = my_paragraph
for old, new in replacements:
    new_paragraph = new_paragraph.replace(old, new)

print (new_paragraph)

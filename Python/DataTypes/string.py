name = "devvrat sharma learning python for agentic ai"
# all the methods of string

print(name[0:10:2])

#partition method: it splits the string into three parts: the part before the separator, the separator itself, and the part after the separator. It returns a tuple containing these three parts.
print(name.partition("learning"))

#__len__ method: it returns the length of the string.
print(name.__len__())

#count() method: it returns the number of occurrences of a substring in the string.
print(name.count("a"))

#find() method: it returns the index of the first occurrence of a substring in the string.
print(name.find("learning"))

label_text = "Devvrat ä"
# decode("utf-8") method: it decodes the bytes-like object to a string using the specified encoding (in this case, UTF-8).
label_text = label_text.encode("utf-8")
print(f"with decoding {label_text}")
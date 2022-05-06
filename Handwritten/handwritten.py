import pywhatkit as pw

txt = """Python is a popular programming language.Python can be used on a server to create web applications.Python works on different platforms (Windows, Mac, Linux, Raspberry Pi, etc).
Python has a simple syntax similar to the English language.
Python has syntax that allows developers to write programs with fewer lines than some other programming languages.
Python runs on an interpreter system, meaning that code can be executed as soon as it is written. This means that prototyping can be very quick.
Python can be treated in a procedural way, an object-oriented way or a functional way."""
pw.text_to_handwriting(txt,"demo1.png",[150,70,150])
print("  END  ")
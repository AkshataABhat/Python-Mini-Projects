import pyshorteners
url=input("Enter the URL: ")
s=
pyshorteners.Shortener().tinyurl.short(url)
print("Your shortened URL is: ",s)

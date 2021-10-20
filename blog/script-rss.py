INSERT_LINE = 15
PUBDATE_LINE = 6

tk_title = input("Title? ")
tk_link = input("Link? ")
tk_description = input("Description? ")
tk_pubdate = input("Pubdate? ")

template = open("script-rss-template.txt")
item = template.read()
template.close()

item = item.replace("tk_title", tk_title)
item = item.replace("tk_link", tk_link)
item = item.replace("tk_description", tk_description)
item = item.replace("tk_pubdate", tk_pubdate)

print(item)

with open("feed.xml", "r") as oldFeed:
    newFeed = oldFeed.readlines()
oldFeed.close()

newFeed.insert(INSERT_LINE, item)
newFeed[PUBDATE_LINE] = f"        <pubDate>{tk_pubdate}</pubDate>\n"

with open("feed.xml", "w") as feed:
    newFeed = "".join(newFeed)
    feed.write(newFeed)
feed.close()

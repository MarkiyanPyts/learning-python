from bs4 import BeautifulSoup

with open('./website.html') as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')
print(soup.title.string)
print(soup.prettify())
print(soup.a)
all_anchor = soup.find_all(name='a')

for link in all_anchor:
    print(link.getText())
    print(link.get('href'))

print(all_anchor)
print(soup.find(name='h1', id='name'))
print(soup.select_one(selector='p a'))
print(soup.select(selector='p a'))
print(soup.select(selector='.heading'))
print(soup.select(selector='#name'))
print(soup.select(selector='p a')[0].getText())
print(soup.select(selector='p a')[0].get('href'))

section_heading = soup.find(name='h3', class_='heading')
print(section_heading.get_text())

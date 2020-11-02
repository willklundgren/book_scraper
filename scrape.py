import requests as r, xml.etree.ElementTree as ET

url = "https://www.audible.com/ep/the-great-courses-scimath?ref=a_ep_the-gr_c5_tab2&pf_rd_p=9728194f-4a29-4ecc-a94b-7b0851ea8c99&pf_rd_r=BMT0NQZ9X7RC6194HDC4"

# html = r.get(url)

# soup = BeautifulSoup(html.content, 'html.parser') # uses Python's built-in HTML parser

# print(soup)

# book_title = input("What's the title?")
book_title = "Thinking, Fast and Slow"

goodreads_url = f"https://www.goodreads.com/search/index.xml/?q={book_title}&key=FqTovm9BJhEeyttHEFkj9Q"

goodreads_response = r.get(goodreads_url)
xml_tree = ET.fromstring(goodreads_response.content)

top_result = xml_tree.find("search").find("results")[0]
top_result_number_of_ratings = top_result[2].text
top_result_avg_rating = top_result[7].text

print(top_result_number_of_ratings, top_result_avg_rating)
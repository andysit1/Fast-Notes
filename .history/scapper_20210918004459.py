def get_link():

    #gets link
    link = entry.get()

    output = ''

    #by using beautiful soup and request we can access the website
    res = requests.get(link)
    html_page = res.content

    soup = BeautifulSoup(html_page, 'html.parser')
    text = soup.find_all(text=True)

    #specific elements we want
    whitelist = [
        'p',
        'li',
    ]

    #specfic characters that we look for
    important_words = [
        '%',
        'cancer',
    ]

    #gets all the text from the p and li elements and formats into string
    for t in text:
        if t.parent.name in whitelist:
            output += '{} '.format(t)
    
    #uses nltk to make the string output into a list of sentences
    a = tokenize.sent_tokenize(output)
    
    #if the sentence has the important_words it saves it into matching
    matching = [s for s in a if any(xs in s for xs in important_words)]
    
    #loops the sentences that are matching and creates a label in our tkinter gui
    for i in range(len(matching)):
        exec('Label%s=Label(window,text="%s", anchor="w", width=720, wraplengt=1000)\nLabel%d.pack()' % (i,matching[i],i))
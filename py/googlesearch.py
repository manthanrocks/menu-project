from googlesearch import search

def scrape_google_search(query):
    
    results = search(query, num_results=5)
    return results


top_results = scrape_google_search('Python programming')
print('Top 5 Google search results:')
for result in top_results:
    print(result)

import requests

def topArticles(limit):
    # Write your code here
    response = requests.get(
        'https://jsonmock.hackerrank.com/api/articles?page=1')
    response = response.json()
    data = list()
    a = lambda x: (x.get('num_comments') if x.get('num_comments') else 0, x.get('title')
                  if x.get('title') else x.get('story_title'))
    data.extend([a(i) for i in response['data']
                if i.get('title') or i.get('story_title')])
    while response['page'] < response['total_pages']:
        response = requests.get(
            f"https://jsonmock.hackerrank.com/api/articles?page={response['page']+1}")
        response = response.json()
        data.extend([a(i) for i in response['data']
                     if i.get('title') or i.get('story_title')])
    data.sort(reverse=True)
    return [i[1] for i in data[:limit]]

if __name__=='__main__':
    limit = int(input('Limit: '))
    print(f'Top {limit} articles are:\n',*[i+'\n' for i in topArticles(limit)])

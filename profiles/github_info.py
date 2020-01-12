import requests
from bs4 import BeautifulSoup as bs

"""
Note, the link to any repo is URL + /RepoName -> myinfo[index]
Literally, to use just:
>>>URL = 'https://github.com/[USERNAME HERE]' (generic github link)
>>>myinfo = git_userinfo(URL, [replacement])
>>>myinfo

{'Name': 'String', 'Username': 'String',
'Repositories': [List] , 'Extra-info': {Following: int ... Projects: int}}

*In the case of an invalid URL, the dictionary
"""


def findall(pattern, master):
    '''Yields all the positions of
    the pattern p in the string s.'''
    i = master.find(pattern)
    while i != -1:
        yield i
        i = master.find(pattern, i + 1)


def create_index(string, sub):
    x = string
    occurence_list = [(i, x[i:i + 2]) for i in findall(sub, x)]

    indices = []
    for tup in occurence_list:
        indices.append(tup[0])
    return (indices)


def repos(string, sub, end_string):
    repositories = []
    size = len(sub)
    indices = create_index(string, sub)

    for index in indices:
        end = string.find(end_string, index + size)
        input_s = string[index + size: end]

        if sub == '<span class="Counter hide-lg hide-md hide-sm">':
            input_s = input_s.strip()

        repositories.append(input_s)
    return repositories


def info(weird):
    keys = ["Repositories", "Projects", "Stars", "Followers", "Following"]
    info_dict = {"Repositories": 0, "Projects": 0,
                 "Stars": 0, "Followers": 0, "Following": 0}

    for key in keys:
        info_dict[key] = weird[keys.index(key)]
    return info_dict


def dictionarify(name, username, repos, extra_info, avatar):

    master_dict = {
        "Name": name,
        "Username": username,
        "Repositories": repos,
        "Extra-info": extra_info,
        "Avi-link": avatar
    }
    return master_dict


def git_getuserinfo2(URL):
    if URL == "":
        return None

    username = URL[19:]

    headers = {
        "User-Agent": "Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H321 Safari/600.1.4"}

    response = requests.get(URL, headers=headers)
    soup = bs(response.text, "html.parser")

    data = soup.prettify()

    """
    f = open('data.txt', 'w', encoding='utf-8')
    f.write(data)
    f.close()
    """

    #get avi link since github uses numbers inconsistently
    counter = 0
    try:
        avi_link = 'https://avatars1.githubusercontent.com/'  + \
            repos(data, '<meta content="https://avatars{0}.githubusercontent.com/' .format(counter), '" ')[0]
    except IndexError:
        try:
            counter += 1
            if counter == 10:
                raise ArithmeticError
            avi_link = 'https://avatars1.githubusercontent.com/'  + \
                repos(data, '<meta content="https://avatars{0}.githubusercontent.com/' .format(counter), '" ')[0]
        except ArithmeticError:
            avi_link = 'https://images.emojiterra.com/twitter/v12/512px/1f418.png'

    userinfo = dictionarify(repos(data, 'data-title="' + username + ' (', ')')[0], username,
                            repos(data, '<span class="repo" title="', '">'), info(
                                repos(data, '<span class="Counter hide-lg hide-md hide-sm">', '</')),
                                avi_link
                            )
    return userinfo

#Built-in error check
def git_userinfo(URL, replace = None):
    try:
        myinfo = git_getuserinfo2(URL)
    except IndexError:
        myinfo = dictionarify(replace, replace, replace, replace, replace)

    return myinfo


"""
    # ------------------Script--------------
URL = "https://github.com/Michael-Kagnew"

myinfo = git_userinfo(URL, "hi")
print(myinfo)

print(myinfo)
print(myinfo["Name"])
print(myinfo["Username"])
print(myinfo["Repositories"])
#Note, the link to any repo is URL + /RepoName -> myinfo[index]
print(myinfo["Extra-info"])
"""

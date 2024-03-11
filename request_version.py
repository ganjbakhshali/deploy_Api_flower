import requests

def get_requests_info():
    version = requests.__version__
    license = requests.__license__
    copyright = requests.__copyright__
    author = requests.__author__
    author_email = requests.__author_email__
    doc_url = requests.__url__
    title = requests.__title__
    description = requests.__description__

    return {
        'Version': version,
        'License': license,
        'Copyright': copyright,
        'Author': author,
        'Author Email': author_email,
        'Documentation URL': doc_url,
        'Title': title,
        'Description': description,
    }

if __name__ == "__main__":
    requests_info = get_requests_info()

    print("Requests Module Information:")
    for key, value in requests_info.items():
        print(f"{key}: {value}")

import requests

def main():
    url = 'http://localhost:8501'
    try:
        r = requests.get(url, timeout=10)
        print('STATUS', r.status_code)
        print((r.text or '')[:1200])
    except Exception as e:
        print('ERROR', repr(e))

if __name__ == '__main__':
    main()

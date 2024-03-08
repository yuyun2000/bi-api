import urllib.request


def get_public_ip():
    url = 'https://api.ipify.org'  # 使用ipify的API获取公网IP
    response = urllib.request.urlopen(url)
    ip = response.read().decode()
    return ip


if __name__ == '__main__':
    public_ip = get_public_ip()
    print(public_ip)
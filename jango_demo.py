import django

print("global print django version:" + django.get_version())

if __name__ == '__main__':
    print(django.get_version())

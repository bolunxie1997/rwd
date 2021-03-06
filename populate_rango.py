import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')
django.setup()
from rango.models import Category, Page


def populate():
    # First, we will create lists of dictionaries containing the pages
    # we want to add into each category.
    # Then we will create a dictionary of dictionaries for our categories. # This might seem a little bit confusing, but it allows us to iterate # through each data structure, and add the data to our models.
    python_pages = [
        {'title': 'Official Python Tutorial',
         'url':'http://docs.python.org/3/tutorial/', 'views':9132},
        {'title':'How to Think like a Computer Scientist',
         'url':'http://www.greenteapress.com/thinkpython/', 'views':5312},
        {'title':'Learn Python in 10 Minutes', 'views':8112,
         'url':'http://www.korokithakis.net/tutorials/python/'}
    ]

    django_pages =[{
            'title':'Official Django Tutorial',
            'url':'https://docs.djangoproject.com/en/2.1/intro/tutorial01/', 'views':412},
            {'title':'Django Rocks',
            'url':'http://www.djangorocks.com/', 'views':112},
            {'title':'How to Tango with Django',
            'url':'http://www.tangowithdjango.com/', 'views':7212}
    ]

    other_pages = [
            {'title':'Bottle',
             'url':'http://bottlepy.org/docs/dev/', 'views':112},
            {'title':'Flask',
             'url':'http://flask.pocoo.org', 'views':6512} ]

    cats = {'Python': {'pages': python_pages, 'likes':64, 'views':128},
                'Django': {'pages': django_pages, 'likes':32, 'views':64},
                'Other Frameworks': {'pages': other_pages, 'likes':16, 'views':32},
            }


    # If you want to add more categories or pages,
        # add them to the dictionaries above.
    # The code below goes through the cats dictionary, then adds each category, # and then adds all the associated pages for that category.
    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data['views'], cat_data['likes'])
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'], p['views'])

    # Print out the categories we have added.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')


def add_page(cat,title,url,views):
    p = Page.objects.get_or_create(category=cat, title=title, views=views)[0]
    p.url=url
    p.views=views
    p.save()
    return p


def add_cat(name, views, likes):
    c = Category.objects.get_or_create(name=name, views=views, likes=likes)[0]
    c.save()
    return c

#Start execution here!
if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()

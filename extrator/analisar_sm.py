import requests
from usp.tree import sitemap_tree_for_homepage



def extrair_sitemap(url):
    tree = sitemap_tree_for_homepage(url)
    sitemap = []
    for page in tree.all_pages():
        sitemap.append(page.url)
    return sitemap

if __name__ == '__main__':
    print(extrair_sitemap('https://www.sympla.com.br/'))
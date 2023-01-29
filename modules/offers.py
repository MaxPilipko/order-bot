import modules.urls as m_urls

ipad = {
    "Title": "IPad",
    "URL": m_urls.ipad,
    "IMG": "images\\ipad.jpg"
}
iphone = {
    "Title": "Iphone",
    "URL": m_urls.iphone,
    "IMG": "images\\iphone.jpg"
}
macbook = {
    "Title": "Mac Book",
    "URL": m_urls.macbook,
    "IMG": "images\\macbook.jpg"
}
apple_watch = {
    "Title": "Apple Watch",
    "URL": m_urls.apple_watch,
    "IMG": "images\\apple_watch.jpg"
}
air_pods = {
    "Title": "Air Pods",
    "URL": m_urls.air_pods,
    "IMG": "images\\air_pods.jpg"
}

offers = [ipad, iphone, macbook, apple_watch, air_pods]
offers_dict = {
    "ipad": ipad,
    "iphone": iphone,
    "macbook": macbook,
    "apple_watch": apple_watch,
    "air_pods": air_pods
}